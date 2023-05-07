import sqlite3
import click

from flask import current_app, g

from flask_sqlalchemy import SQLAlchemy

from flaskr.classes import position as p

db = SQLAlchemy()

def add_position_to_db(position):
    db.session.add(position)
    db.session.commit()

def get_all_positions_from_db():
    return p.Position.query.all()


""" DEPRECATED, ONLY WORKS WITH SQLITE3
    def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
def init_db_command():
    "/"/"/Clear the existing data and create new tables."/"/"/
    init_db()
    click.echo('Initialized the database.')

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

def add_to_db(tableName, obj):
    query = ''
    
    return"""