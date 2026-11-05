import sqlite3

conn = sqlite3.connect('app.db')
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        status TEXT DEFAULT 'new'
    )
""")

conn.commit()
conn.close()
print('База данных и таблица tasks успешно созданы.')
