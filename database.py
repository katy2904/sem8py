import pandas as pd
import UI


# использовала для создания заголовков в соответствующих файлах
# basic = pd.DataFrame(columns = ['ID', 'Фамилия', 'Имя', 'Отчество', 'Дата рождения', 'Телефон', 'Домашний адрес'])
# job = pd.DataFrame(columns = ['ID', 'Дата приема на работу', 'Подразжеление(отдел)', 'Должность'])
# salary = pd.DataFrame(columns = ['ID', 'Оклад', 'Премия'])

# basic.to_csv('basic.csv')
# job.to_csv('job.csv')
# salary.to_csv('salary.csv')

def create_df(data):
    return pd.DataFrame(data)

def into_db(file, df):
    df.to_csv(file, mode='a', index=False, header=False)

def from_db(file, data):
    data = pd.read_csv(file)
    data.head(10)

def read_csv(file):
    result = pd.read_csv(file, index_col=0)
    return result

def concat_base(file1, file2, file3):
    df1 = read_csv(file1)
    df2 = read_csv(file2)
    df3 = read_csv(file3)
    # final_db = pd.merge(df1, df2, df3)
    final = pd.concat([df1, df2, df3], axis=1, join='inner')
    final = final.reset_index()
    return final

def search_db(db, column, param):
    df_new = db[db[column] == param]
    UI.view_data(df_new)

