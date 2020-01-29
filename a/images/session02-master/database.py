import sqlite3

conn = sqlite3.connect('test.db')

conn.execute('''CREATE TABLE USERS
         (
         username           TEXT    NOT NULL,
         password            TEXT     NOT NULL,
         email        TEXT,
         contact         INT);''')

conn.close()
