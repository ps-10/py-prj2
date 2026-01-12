import pandas as pd  #need a library openpyxl

file1 = r"C:\Users\prade\PycharmProjects\py-prj2\replace-data.xlsx"
df1 = pd.read_excel(file1)
print('---------before-------------')
print(df1.head())
print('---------*after*-------------')
# replace the value in 'tag' column, within the df
df1['tag'] = df1['tag'].replace('actg-2024','actg-2026')
print(df1.head())
# now update the excel file using the method "to.excel"
df1.to_excel(file1, index=False) # do not write df index as the first column in excel