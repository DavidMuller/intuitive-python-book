import contextlib
import sqlite3


with sqlite3.connect("example.db") as connection:
    with contextlib.closing(connection.cursor()) as cursor:
        cursor.execute("CREATE TABLE IF NOT EXISTS allowed (name text)")
        cursor.execute("INSERT INTO allowed values ('Arthur')")
        cursor.execute("INSERT INTO allowed values ('Lancelot')")
        cursor.execute("SELECT name from allowed")
        print(cursor.fetchall())
