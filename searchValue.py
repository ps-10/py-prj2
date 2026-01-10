import pandas as pd

df1 = pd.read_csv(r"C:\Users\prade\PycharmProjects\py-prj2\titanic-full.csv")  # load csv to df
search_values = ['Pradeep', 'Divya', 'Neil']
df2 = df1[df1.isin(search_values).any(axis=1)]  #see below

# pandas show every row that has the value 'Pradeep' somwehere inside it
# df.eq does comparison of each cell
# .any(axis=1): outputs only the col where this value exists times number of rows. if so, write a boolean 1
# the output is a data frame series of rows where the target value exists
# output assigned to df1

pd.set_option('display.max_columns', None)  # to not truncate columns
print(df2)
