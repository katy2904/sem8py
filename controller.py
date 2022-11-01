import database as db
import logger as log
import UI
import operation as op

marker = True
def pushbutton():
    log.log_data('Старт программы')
    UI.view_data('База данных сотрудников предприятия')
    global marker
    while True:
        choice = UI.choice()
        match choice:
            case 1:
                op.new_inf()
                UI.resume()
            case 2:
                op.search_inf()
                UI.resume()
            case 3:
                UI.view_data(db.concat_base('basic.csv', 'job.csv', 'salary.csv'))
                log.log_data('Просмотр сводной таблицы')
                UI.resume()
            case 4:
                log.log_data('Выход из программы')
                exit()



