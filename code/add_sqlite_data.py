import contextlib
import sqlite3


with sqlite3.connect("example.db") as connection:  # <label id="code.add_sqlite_data.connection"/>
    with contextlib.closing(connection.cursor()) as cursor:  # <label id="code.add_sqlite_data.cursor"/>
        cursor.execute("CREATE TABLE IF NOT EXISTS knights (name text)")  # <label id="code.add_sqlite_data.statements"/>
        cursor.execute("INSERT INTO knights values ('Arthur')")
        cursor.execute("INSERT INTO knights values ('Lancelot')")
        cursor.execute("SELECT name from knights")
        print(cursor.fetchall())
