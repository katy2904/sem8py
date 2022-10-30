def get_data(text):
    return input(text)

def view_data(data):
    print(data)


def choice():
    print('База данных сотрудников предприятия')
    print('Возможные действия:\n'
          '   1 - новая запись в справочник\n'
          '   2 - поиск информации по справочнику\n'
          '   3 - распечатать весь справочник\n'
          '   4 - выход из программы')
    flag = False
    while flag == False:
        select = input()
        try:
            if 1 <= int(select) <= 4:
                return int(select)
            else:
                flag = False
                print('Недопустимое действие, уточните запрос')
        except:
            flag = False
            print('Недопустимое действие, уточните запрос')
    return select