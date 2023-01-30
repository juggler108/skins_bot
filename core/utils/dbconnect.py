import sqlite3 as sq


async def add_data_sqlite(user_id, user_name):
    db = sq.connect('sqlitedb.db')
    mycursor = db.cursor()
    myresult = mycursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id, )).fetchall()
    if not myresult:
        mycursor.execute("INSERT INTO users (user_id, user_name) VALUES (?, ?)", (user_id, user_name))
        db.commit()
