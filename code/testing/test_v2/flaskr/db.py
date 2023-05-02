import sqlite3

import click
from flask import current_app, g


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

def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

import sqlite3

def dump_sqlite_to_txt(db_filename, txt_filename):
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()
    
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    with open(txt_filename, 'w') as f:
        for table_name in tables:
            f.write("Table: {}\n".format(table_name[0]))
            cursor.execute("SELECT * from {}".format(table_name[0]))
            headers = [description[0] for description in cursor.description]
            f.write("\t".join(headers) + "\n")
            rows = cursor.fetchall()
            for row in rows:
                f.write("\t".join(str(field) for field in row) + "\n")
    
    cursor.close()
    conn.close()