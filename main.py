import pandas as pd
import numpy as np
from data_clean_function import cleandata
from search import search
from model_selector import print_car_details
from data_visualisation3 import data_visualisation3
from mean_brand_price import MeanBrandPrice



# Read the CSV file into a pandas DataFrame
spreadsheet = 'cars.csv'
df = pd.read_csv(spreadsheet)


cleaner = input("Clean Data? Enter y/n: ")

if cleaner == ("y"):
    df = cleandata(spreadsheet)
elif cleaner == ("n"):
    print("This step has been skipped")
else:
    print("Invalid input, skipping")

# Extract unique values from the "Brand" column
unique_brands = np.unique(df['Brand'])
#case insensitive user input for "Brand" value
brand = search(unique_brands,'brand')
# Extract the rows where the value in the "Brand" column is equal to the desired brand
brand_df = df.loc[df["Brand"] == brand]
print("Mean Price of " + brand + " vehicles: "+str(MeanBrandPrice(df,brand,2,'Mean')))
print("Median Price of " + brand + " vehicles: "+str(MeanBrandPrice(df,brand,2,'Median')))
print("Mode Price of " + brand + " vehicles: "+str(MeanBrandPrice(df,brand,2,'Mode')))
# Get unique models for the chosen brand
unique_models = np.unique(brand_df['Model'])

model = search(unique_models,'model')

# Extract the rows where the value in the "Model" column is equal to the desired model
model_df = brand_df.loc[brand_df["Model"] == model]


# Take user input for price range
#Exits loop when valid number is provided
while not 'price_min' in locals():
    try:
        price_min = float(input("Enter minimum price: "))
    except:
        print("Invalid number provided")
while not 'price_max' in locals():
    try:
        price_max = float(input("Enter maximum price: "))
    except:
        print("Invalid number provided")
# Extract the rows where the value in the "Price" column is between the price range
price_range_df = model_df.loc[(model_df["Price"] >= price_min) & (model_df["Price"] <= price_max)]

# Display the search result
print(price_range_df)

# Extract the values from the "Model" column for the rows in brand_df
print_car_details()

visualisation = input("Do you want a Visualisation on our data y/n: ")
if visualisation == "y":
    data_visualisation3()
else:
    print("Program is shutting down")
    exit()