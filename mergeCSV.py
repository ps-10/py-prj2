import pandas as pd

# loading the data
file1 = r"C:\Users\prade\PycharmProjects\py-prj2\titanic.csv"
file2 = r"C:\Users\prade\PycharmProjects\py-prj2\titanic-d1.csv"  # delta file path
df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)  # load both files to individual dataframes
df3 = pd.concat([df1, df2], ignore_index=True)
    # df that holds combined data
    # ignore_index excludes the row numbers
df3.to_csv(r'C:\Users\prade\PycharmProjects\py-prj2\titanic-full.csv', index=False)
    # to.csv writes a df to csv.
    # dont
    # index=False tells pandas not to write the row index numbers to the file
    # write 'r' to give true path to the combined file
