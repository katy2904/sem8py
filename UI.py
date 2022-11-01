import logger as log
import operation as op

def get_data(text):
    return input(text)

def view_data(data):
    print(data)


def choice():
    view_data('Возможные действия:\n'
              '   1 - новая запись в справочник\n'
              '   2 - поиск информации по справочнику\n'
              '   3 - распечатать весь справочник\n'
              '   4 - выход из программы')
    select = op.check_selekt(1, 4)
    return select


def data_basic():
    pid = op.ID('basic.csv')
    view_data(pid)
    basic_dict= {'ID': [pid],
                 'Фамилия': [input('Фамилия: ')], 'Имя': [input('Имя: ')], 'Отчество': [input('Отчество: ')],
                 'Дата рождения': [input('Дата рождения: ')], 'Телефон': [input('Телефон: ')],
                 'Домашний адрес': [input('Домашний адрес: ')]}
    return basic_dict

def data_job():
    pid = op.ID('job.csv')
    job_dict = {'ID': [pid], 'Дата приема на работу': [input('Дата приема на работу: ')],
                'Подразделение(отдел)': [input('Подразделение(отдел): ')],
                'Должность': [input('Должность: ')]}
    return job_dict

def data_salary():
    pid = op.ID('salary.csv')
    salary_dict = {'ID': [pid], 'Оклад': [input('Оклад: ')], 'Премия': [input('Премия: ')]}
    return salary_dict

def search_info():
    view_data('Возможные варианты поиска:\n'
              '   1 - по фамилии\n'
              '   2 - по имени\n'
              '   3 - по дате рождения\n'
              '   4 - по телефону\n'
              '   5 - по подразделению(отделу)\n'
              '   6 - по должности\n'
              '   7 - по окладу\n'
              '   8 - по премии')
    search_var = op.check_selekt(1, 7)
    return search_var

def resume():
    view_data('Продолжить работу со справочником?:\n'
              '   1 - да\n'
              '   2 - нет\n')
    select = op.check_selekt(1, 2)
    match select:
        case 1: return True
        case 2:
            log.log_data('Выход из программы')
            exit()
            return False