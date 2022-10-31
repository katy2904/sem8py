import logger as log
import numpy
import pandas as pd
import UI
import database as db


def check_selekt(a, b):
    flag = False
    while flag == False:
        option = input()
        try:
            if a <= int(option) <= b:
                return int(option)
            else:
                flag = False
                UI.view_data('Недопустимое действие, уточните запрос')
        except:
            flag = False
            UI.view_data('Недопустимое действие, уточните запрос')
    return int(option)


def ID(file):
    id = len(db.read_csv(file)) + 1
    return id

def new_inf():
    db.into_db('basic.csv', UI.data_basic())
    db.into_db('job.csv', UI.data_job())
    db.into_db('salary.csv', UI.data_salary())
    log.log_data('Внесены новые данные в базу')


def search_inf():
    search_base = db.concat_base('basic.csv', 'job.csv', 'salary.csv')
    search_option = UI.search_info()
    match search_option:
        case 1: column, param = 'Фамилия', UI.get_data('Введите фамилию: ')
        case 2: column, param = 'Имя', UI.get_data('Введите имя: ')
        case 3: column, param = 'Дата рождения', UI.get_data('Введите дату рождения: ')
        case 4: column, param = 'Телефон', UI.get_data('Введите телефон: ')
        case 5: column, param = 'Подразжеление(отдел)', UI.get_data('Введите подразделение(отдел): ')
        case 6: column, param = 'Должность', UI.get_data('Введите должность: ')
        case 7: column, param = 'Оклад', UI.get_data('Введите размер оклада: ')
        case 8: column, param = 'Премия', UI.get_data('Введите размер премии: ')
    log.log_data(f'Поиск данных по запросу{param}')
    db.search_db(search_base, column, param)
