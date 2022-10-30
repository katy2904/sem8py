from datetime import datetime as dt


def log_data(data):
    time = dt.now().strftime('%d.%m.%Y - %H:%M:%S')
    with open('Log.txt', 'a', encoding="utf-8") as file:
        file.write(f'{time}: Info: {data}\n')