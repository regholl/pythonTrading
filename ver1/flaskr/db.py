import os
import sqlite3

import click
from flask import current_app, g
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

db = SQLAlchemy()
current_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(os.path.join(current_app.instance_path, 'flaskr.sqlite'))

def get_db():
    if not hasattr(g, 'db'):
        db_uri = current_app.config['SQLALCHEMY_DATABASE_URI']
        engine = create_engine(db_uri)
        g.db = engine.connect()
    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

@click.command('init-db')
def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.execute(f.read().decode('utf8'))

def init_app(app):
    db.init_app(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(os.path.join(current_app.instance_path, 'flaskr.sqlite'))
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db)

def dump_sqlite_to_txt(db_filename, txt_filename):
    engine = create_engine('sqlite:///{}'.format(db_filename))
    connection = engine.connect()

    tables = connection.execute("SELECT name FROM sqlite_master WHERE type='table';")
    
    with open(txt_filename, 'w') as f:
        for table_name in tables:
            f.write("Table: {}\n".format(table_name[0]))
            result = connection.execute("SELECT * from {}".format(table_name[0]))
            headers = [col for col in result.keys()]
            f.write("\t".join(headers) + "\n")
            rows = result.fetchall()
            for row in rows:
                f.write("\t".join(str(field) for field in row) + "\n")
    
    connection.close()

