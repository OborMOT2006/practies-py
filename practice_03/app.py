from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return """
    <html>
        <head><meta charset="UTF-8"><title>Список задач</title></head>
        <body>
            <h1>Мой список задач</h1>
            <p>Позже здесь будут задачи из базы.</p>
            <a href="/about">О проекте</a>
        </body>
    </html>
    """


@app.route('/about')
def about():
    return 'Учебный список задач на Flask. Практическая работа №3.'


if __name__ == '__main__':
    app.run(debug=True, port=5000)
