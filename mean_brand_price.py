import numpy as np
import statistics
def MeanBrandPrice(df,brand,pricecolumnnumber,operation):
    #create empty variable
    sumofvalues = 0
    values = []
    #find the row of all values of brand
    wherebrand = np.where(df.values == brand)
    #find price for each vehicle and add it to a variable
    for i in range(len(wherebrand[0])):
        value = df.iat[wherebrand[0][i],pricecolumnnumber]
        sumofvalues = sumofvalues + value
        values.append(value)
    #take the average
    if operation == 'Mean':
        brandaverage = round(sumofvalues/len(wherebrand[0]))
    elif operation == 'Median':
        brandaverage = int(statistics.median(values))
    elif operation == 'Mode':
        brandaverage = int(statistics.mode(values))
    return brandaverage