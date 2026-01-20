import pandas as pd  #need a library openpyxl

#----------- set pandas
pd.set_option('display.max_columns', None)  # to not truncate columns
pd.set_option('display.max_rows', None)  # to not truncate rows
#----------- read file
file1 = r"C:\Users\prade\PycharmProjects\py-prj2\replace-data.xlsx"
df1 = pd.read_excel(file1)
print(df1.head())
#----------- change data
# replace the value in 'tag' column, within the df
df1['tag'] = df1['tag'].replace('actg-2024','actg-2026')
# convert the price to standard 2-digit decimal using
df1['price'] = df1['price'].round(2)
# convert the date into std format YYYY-MM-DD using pandas datetime object
# https://pandas.pydata.org/pdeps/0004-consistent-to-datetime-parsing.html
df1['date'] = pd.to_datetime(df1['date'], format='%m%d%Y').dt.strftime('%Y%m%d')
print(df1.head())
#----------- write results to new file
# now update the excel file using the method "to.excel"
# do not write df index as the first column in excel
file2 = r"C:\Users\prade\PycharmProjects\py-prj2\replaced-data.csv"
df1.to_csv(file2, index=False)