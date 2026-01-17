import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# print(pd.__version__)
# print(mp.__version__)
# print(sns.__version__)

df = pd.read_csv(r"C:\Users\prade\PycharmProjects\py-prj2\titanic-full.csv")  # load csv to df

plt.figure(figsize=(8,6))
sns.stripplot(data=df, x='Sex', y='Age')
# sns.boxplot(data=df,x='Sex',y='Age')
# sns.violinplot(data=df,x='Sex',y='Age')
plt.show()
