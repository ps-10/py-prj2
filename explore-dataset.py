import pandas as pd

# loading the data
file_path = r"C:\Users\prade\PycharmProjects\py-prj2\titanic-full.csv"
df = pd.read_csv(file_path)
'''
# display rows to confirm data loaded successfully
'''
'''
print(df.head())  # show top rows w/ truncate columns to confirm data load
print('--------')
print(df.columns)  # show list of all columns
print('--------')
pd.set_option('display.max_columns', None)
print(df.head())  # show top rows w/ ALL columns to confirm data load
print('-------- decsription -------- ')
print(df.describe())
'''
print('-------- distinct values -------- ')
#print(df['Sex'].value_counts())  # shows unique values in col. sex, and count of such values
#print(df.info(), df.isnull().sum())
print('-------- null values -------- ')
print(df[df['Sex'].isnull()])
# print(df.isnull().any(axis=1))  # return rows with any null values