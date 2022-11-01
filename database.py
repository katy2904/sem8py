import pandas as pd

# def create_db():
#     basic = pd.DataFrame(columns = ['ID', 'Фамилия', 'Имя', 'Отчество', 'Дата рождения', 'Телефон', 'Домашний адрес'])
#     job = pd.DataFrame(columns = ['ID', 'Дата приема на работу', 'Подразжеление(отдел)', 'Должность'])
#     salary = pd.DataFrame(columns = ['ID', 'Оклад', 'Премия'])
#
#     basic.to_csv('basic.csv')
#     job.to_csv('job.csv')
#     salary.to_csv('salary.csv')

def create_df(data):
    return pd.DataFrame(data)

def into_db(file, df):
    df.to_csv(file, mode='a', index=False, header=False)

def from_db(file, data):
    data = pd.read_csv(file)
    data.head(10)

def read_csv(file):
    result = pd.read_csv(file)
    return result

def concat_base(file1, file2, file3):
    final_db = pd.concat([read_csv(file1), read_csv(file2), read_csv(file3)], axis=1, join='inner')
    return final_db

def search_db(db, column, param):
    print(db[db[column] == param])

