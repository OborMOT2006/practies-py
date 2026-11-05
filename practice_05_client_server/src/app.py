import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


def get_connection():
    conn = sqlite3.connect('app.db')
    conn.row_factory = sqlite3.Row
    return conn


def fetch_all_tasks():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id, title, status FROM tasks ORDER BY id')
    rows = cursor.fetchall()
    conn.close()
    return rows


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        if not title:
            return render_template('index.html', items=fetch_all_tasks(),
                                   error='Название не может быть пустым.')

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO tasks (title) VALUES (?)', (title,))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    return render_template('index.html', items=fetch_all_tasks())


if __name__ == '__main__':
    app.run(debug=True, port=8081)
