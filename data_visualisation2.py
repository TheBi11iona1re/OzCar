#Data Visualization: Plot a bar graph to compare the average price of this """""vehicle""""" in the last 2 years.
#'this vehicle' is understood as same model
#'last 2 years' is understood as last two years available from the last year of the model
#this is not finished or working
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mean_brand_price import MeanBrandPrice

def data_visualisation(df,model):
    #Create empty list
    yearsofmodel = []
    meanprice = 0
    wheremodel = np.where(df['Model'].values == model)
    print (wheremodel)
    for i in range(len(wheremodel[0])):
        yearsofmodel.append(df.iat[wheremodel[0][i],7])
    uniqueyearsofmodel = list(set(yearsofmodel))
    uniqueyearsofmodel.sort(reverse=True)
    lasttwoyearsofmodel = uniqueyearsofmodel[0:3]
    for i in range(len(uniqueyearsofmodel)):
        fortnite = np.where(df['Year'].values == yearsofmodel[i])
        for i in range(len(fortnite)):
            meanprice = meanprice + df.iat[fortnite[0][i],2]
        meanprice = meanprice/len(fortnite)
        print(meanprice.round())
    
    print(lasttwoyearsofmodel)
    for i in range(len(lasttwoyearsofmodel)):
        print(df.iat[lasttwoyearsofmodel[i],2])


