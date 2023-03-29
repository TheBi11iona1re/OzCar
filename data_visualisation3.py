#genius naming scheme explained:
#data_visulisation3 shows a bar graph of the average price for each brand
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mean_brand_price import MeanBrandPrice

def data_visualisation3():
    spreadsheet = 'cars.csv'
    df = pd.read_csv(spreadsheet)


    # Extract unique values from the "Brand" column
    unique_brands = np.unique(df['Brand'])

    #Create empty list
    averagepricebybrand = []
    for i in range(len(unique_brands)):
        meanprice = MeanBrandPrice(df,unique_brands[i],2,'Mean')
        averagepricebybrand.append(meanprice)
    #Graph of Average Price by Brand
    #Make graph fit in window
    plt.figure(figsize=(15, 5))
    plt.bar(unique_brands,averagepricebybrand)
    #Make value labels vertical so they are easier to read
    plt.xticks(rotation=90)
    plt.savefig('my_plot.png')

#! go to my_plot.png to see the finished graph



