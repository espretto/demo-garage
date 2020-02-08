
import sqlite3

from flask import g


DB_FILEPATH = './database/garage.db'


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DB_FILEPATH)
        g.db.row_factory = sqlite3.Row

        # enforce foreign key constraints for this connection
        # unfortunately this setting does not persist and has
        # to be renewed on every connection
        with g.db as con:
            con.execute('PRAGMA foreign_keys=ON')
    
    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
