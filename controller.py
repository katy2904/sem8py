import database as db
import logger as log
import UI
import operation as op

def pushbutton():
    log.log_data('Старт программы')
    choice = UI.choice()
    match choice:
        case 1: op.new_inf()
        case 2: op.search_inf()
        case 3:
            UI.view_data(db.concat_base('basic.csv', 'job.csv', 'salary.csv'))
            log.log_data('Просмотр сводной таблицы')
        case 4:
            log.log_data('Выход из программы')
            quit()



pushbutton()