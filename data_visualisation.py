300300#test module 
#Data Visualization: Plot a bar graph to compare the average price of this vehicle in the last 2 years. 
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('cars.csv')
columns = df.columns

print("The number of samples in dataset: {}".format(df.shape[0]))
for column in columns:
    print(column, " unique size: {}".format(df[column].unique().size))
    
    if df[column].unique().size == df.shape[0]:
        print(column, ": Unnecessary Column. Delete from the dataset.")
        df = df.drop(labels=column, axis=1)
        print("himmm")

# using matplotlib

# Get the top 20 companies
company_top20 = (df.groupby('Brand').size().reset_index(name='counts').sort_values(by='counts', ascending=False).head(20))
#
plt.figure(figsize=(18, 5))
sns.barplot(x=company_top20.Brand, y=company_top20.counts) #, palette=Set2
plt.xlabel('Company Name')
plt.ylabel('Number of cars')
plt.xticks(rotation=45)
plt.show()

