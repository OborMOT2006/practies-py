import sqlite3
from flask import Flask, render_template

app = Flask(__name__)


def get_connection():
    conn = sqlite3.connect('app.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id, title, status FROM tasks ORDER BY id')
    rows = cursor.fetchall()
    conn.close()
    return render_template('index.html', items=rows)


if __name__ == '__main__':
    app.run(debug=True, port=8081)
