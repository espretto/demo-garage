
import sqlite3
import glob
import os


def relative(path):
    return os.path.join(os.path.dirname(__file__), path)


DB_FILEPATH=relative('garage.db')


def exec_script(sql):
    connection = sqlite3.connect(DB_FILEPATH)
    try:
        connection.cursor().executescript(sql)
        connection.commit()
    except sqlite3.Error as err:
        print(err)
    finally:
        connection.close()


def remove_db():
    if os.path.exists(DB_FILEPATH):
        os.remove(DB_FILEPATH)


def create_db():
    for scriptpath in sorted(glob.glob(relative('*.sql'))):
        with open(scriptpath, 'r') as scriptfile:
            exec_script(scriptfile.read())


if __name__ == '__main__':
    remove_db()
    create_db()