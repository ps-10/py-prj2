import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# create a list of companies less than the  PE ratio specified by the user ..
# & see a histogram distribution of the same. data downloaded from kaggle.

#-------------
pd.set_option('display.max_columns', None)  # to not truncate columns
pd.set_option('display.max_rows', None)  # to not truncate rows

#------------- data load, cleanup
file1 = r"C:\Users\prade\PycharmProjects\py-prj2\PE.csv"  # read source data with PE values
df1 = pd.read_csv(file1)  # store to dataframe
df1['Price/Earnings']= round(df1['Price/Earnings'],2)  # round all PE ratios to 2 decimals
print(df1.head())  # check if file load was correct

#-------------- user prompts
sector = input("Enter your sector name: ")  # user input for sector name
max_PE = round(float(input("Enter your max PE: ")),2)  # user input for max PE

#-------------- data filters
condition = (df1['Sector'] == sector) & (df1['Price/Earnings'] < max_PE)  # create a variable condition to store all conditions
filtered_df1 = df1[condition]  # filter the dataframe based on conditions
print(filtered_df1.head())  # check if filtering worked
filtered_df1 = filtered_df1.sort_values(by='Price/Earnings', ascending=False)  # sort df by descending PE
file2 = r"C:\Users\prade\PycharmProjects\py-prj2\PE_filtered.csv"
    # file path for the new filtered records
filtered_df1.to_csv(file2, index=False)   # write filtered records to a new file

#-------------- data plots (histogram)
my_bins = [0, 3, 7, 11, 15, 19, 23]  # i defined the bin sizes
sns.histplot(data = filtered_df1, x = 'Price/Earnings', bins = my_bins)
    # plot the filtered df on a histogram
plt.xlabel('PE')
plt.ylabel('Count')
plt.title('PE Distribution')
plt.xticks(my_bins)
plt.show()