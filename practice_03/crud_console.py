import sqlite3


def get_connection():
    return sqlite3.connect('app.db')


def show_menu():
    print('\n===== СПИСОК ЗАДАЧ =====')
    print('1. Показать все задачи')
    print('2. Добавить задачу')
    print('3. Отметить выполненной')
    print('4. Удалить задачу')
    print('0. Выход')


def list_tasks():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id, title, status FROM tasks ORDER BY id')
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print('Список пока пуст.')
        return
    for task_id, title, status in rows:
        print(f'{task_id}. {title} [{status}]')


def add_task():
    title = input('Название задачи: ').strip()
    if not title:
        print('Название не может быть пустым.')
        return
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (title) VALUES (?)', (title,))
    conn.commit()
    print(f'Добавлена задача номер {cursor.lastrowid}')
    conn.close()


def mark_done():
    list_tasks()
    raw = input('Номер задачи: ').strip()
    if not raw.isdigit():
        print('Нужно ввести число.')
        return
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET status = 'done' WHERE id = ?", (int(raw),))
    conn.commit()
    print('Задача обновлена.' if cursor.rowcount else 'Такой задачи нет.')
    conn.close()


def delete_task():
    list_tasks()
    raw = input('Номер для удаления: ').strip()
    if not raw.isdigit():
        print('Нужно ввести число.')
        return
    if input('Точно удалить? (y/n): ').strip().lower() != 'y':
        print('Отмена.')
        return
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = ?', (int(raw),))
    conn.commit()
    print('Задача удалена.' if cursor.rowcount else 'Такой задачи нет.')
    conn.close()


def main():
    while True:
        show_menu()
        choice = input('Действие: ').strip()
        if choice == '1':
            list_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            mark_done()
        elif choice == '4':
            delete_task()
        elif choice == '0':
            print('Выход.')
            break
        else:
            print('Нет такого пункта.')


if __name__ == '__main__':
    main()
