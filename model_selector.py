import pandas as pd

def print_car_details():
  # Read the CSV file into a pandas DataFrame
  spreadsheet = 'cars.csv'
  df = pd.read_csv(spreadsheet)
  found = False
  while not found:
    try:
      SelectedModel = int(input("Enter the row of the Car you want more details on: "))
      # Print row by index position
      print(df.loc[SelectedModel])
      #make loop end once valid row provided
      found = True
    except:
      print("Invalid model provided, please try again")