import sqlite3 as sq


db = sq.connect('sqlitedb.db')
cur = db.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, user_id VARCHAR(255), user_name VARCHAR(255))")
