import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# create a list of companies less than the  PE ratio specified by the user & see a histogram distribution of the same

#-------------
pd.set_option('display.max_columns', None)  # to not truncate columns

#------------- data load, cleanup
file1 = r"C:\Users\prade\PycharmProjects\py-prj2\PE.csv"  # read source data with PE values
df1 = pd.read_csv(file1)  # store to dataframe
df1['PE']= round(df1['PE'],2)  # round all PE ratios to 2 decimals
print(df1.head())  # check if file load was correct

#-------------- user prompts
country = input("Enter your company origin name: ")  # user input for company origin name
max_PE = round(float(input("Enter your max PE: ")),2)  # user input for max PE

#-------------- data filters
filtered_df1 = df1[(df1['Company Origin'] == country) & (df1['PE'] < max_PE)]  # filter the dataframe
print(filtered_df1.head())  # check if filtering worked
filtered_df1 = filtered_df1.sort_values(by='PE', ascending=False)  # sort df by descending PE
file2 = r"C:\Users\prade\PycharmProjects\py-prj2\PE_filtered.csv"  # file path for the new filtered records
filtered_df1.to_csv(file2, index=False)   # write filtered records to a new file

#-------------- data plots (histogram)
my_bins = [0, 3, 7, 12]  # i defined the bin sizes
sns.histplot(data = filtered_df1, x = 'PE', bins = my_bins, color = 'blue')  # plot the filtered df on a histogram
plt.xlabel('PE')
plt.ylabel('Count')
plt.title('PE Distribution')
plt.xticks(my_bins)
plt.show()