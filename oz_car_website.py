import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os 


# Importing the data_clean_function module from the same directory
from data_clean_function import cleandata

# Importing the search module from the same directory
from search import search

# Importing the print_car_details module from the same directory
from model_selector import print_car_details

# Importing the MeanBrandPrice class from the same directory
from mean_brand_price import MeanBrandPrice

# Importing the data_visualisation module from the same directory
from data_visualisation2 import data_visualisation

# Importing session from Flask
from flask import session

# Importing data statistics for live data
from mean_brand_price import MeanBrandPrice


# Reading in the cars.csv file into a pandas dataframe
global spreadsheet
spreadsheet = 'cars.csv'
df = pd.read_csv(spreadsheet)

global selected_brand
global results
selected_brand = None

#* Flask server initiation 
# TODO: Create a Flask server to host the website that will be used to display the data this is just a test server 


from flask import Flask, redirect, url_for, render_template, session, request
app = Flask(__name__)
os.environ['FLASK_APP'] = 'oz_car_website.py' 

#*this is for the search function
@app.route('/big_data', methods=['POST'])
def big_data():
    global selected_brand
    data = pd.read_csv("cars.csv")
    selected_brand = request.form.get('brand')
    filtered_data = data[(data['Brand'] == selected_brand)]
    filtered_data.to_csv('brand.csv', index=False)
    return render_template('big_data.html', tables=[filtered_data.to_html(classes='table table-bordered table-hover table-sm table')], titles=[''])

#*this is for the search function
@app.route('/big_data_two', methods=['POST'])
def big_data_two():
    df = pd.read_csv('brand.csv')
    options = [{'label': i, 'value': i} for i in df['Model'].unique()]
    selected_model = request.form.get('model')
    filtered_data2 = df[(df['Model'] == selected_model)]
    filtered_data2.to_csv('model.csv', index=False)
    mean = ("Mean Price of " + selected_brand + " vehicles: "+str(MeanBrandPrice(df,selected_brand,2,'Mean')))
    median = ("Median Price of " + selected_brand + " vehicles: "+str(MeanBrandPrice(df,selected_brand,2,'Median')))
    mode = ("Mode Price of " + selected_brand + " vehicles: "+str(MeanBrandPrice(df,selected_brand,2,'Mode')))
    return render_template('big_data_two.html', mean=mean, median=median, mode=mode, options=options, tables=[filtered_data2.to_html(classes='data table table-bordered table-hover table-sm')], titles=df.columns.values)

#*this is for the search function
@app.route('/big_data_twoo', methods=['POST'])
def big_data_twoo():
    return render_template('big_data_twoo.html')

#*this is for the search function
@app.route('/big_data_three', methods=['POST'])
def big_data_three():
    print("BIG DATA THREE")
    df = pd.read_csv('model.csv')
    price_min = request.form.get('minprice')
    price_max = request.form.get('maxprice')
    price_min = int(price_min)
    price_max = int(price_max)
    filtered_data3 = df[(df['Price'] >= price_min) & (df['Price'] <= price_max)]
    filtered_data3.to_csv('results.csv', index=False)
    return render_template('big_data_three.html', tables=[filtered_data3.to_html(classes='data table table-bordered table-hover table-sm')], titles=df.columns.values)

#*this is for the search function
@app.route('/specifics', methods=['POST'])
def miscellaneous():
    return render_template('specifics.html',)

#*this is for the search function
@app.route('/results', methods=['POST'])
def results():
    input_questions = {
        "brand_input": "Brand",
        "model_input": "Model",
        "series_input": "Series",
        "variant_input": "Variant",
        "colour_input": "Color",
        "year_input": "Year",
        "status_input": "Status",
        "gearbox_input": "Gearbox",
        "fuel_input": "Fuel",
        "price_max": "Price",
        "price_min": "Price",
        "kilometers_input": "Kilometers",
        "cc_input": "CC",
        "seat_input": "Seating Capacity"
    }
        
    
    df = pd.read_csv("results.csv")
    series = request.form['series']
    variant = request.form['variant']
    year = int(request.form['year']) if request.form['year'] else None
    status = request.form['status']
    gearbox = request.form['gearbox']
    fuel = request.form['fuel']
    kilometers = int(request.form['kilometers']) if request.form['kilometers'] else None
    cc = int(request.form['cc']) if request.form['cc'] else None
    seatingcapacity = int(request.form['seatingcapacity']) if request.form['seatingcapacity'] else None
    color = request.form['color']


    results = df.copy()
    
    if series:
        results = results[results['Series'] == series]

    if variant:
        results = results[results['Variant'] == variant]

    if year:
        results = results[results['Year'] == year]

    if status:
        results = results[results['Status'] == status]

    if gearbox:
        results = results[results['Gearbox'] == gearbox]

    if fuel:
        results = results[results['Fuel'] == fuel]

    if color:
        results = results[results['Color'] == color]

    if kilometers:
        results = results[results['Kilometers'] <= kilometers]

    if cc:
        results = results[results['CC'] <= cc]

    if seatingcapacity:
        results = results[results['Seating Capacity'] <= seatingcapacity]
    
    if color:
        results = results[results['Color'] == color]
        results.to_csv('results2.csv', index=False)
        
    if kilometers:
        results = results[results['Kilometers'] <= kilometers]
        results.to_csv('results2.csv', index=False)
        
    if cc:
        results = results[results['CC'] <= cc]
        results.to_csv('results2.csv', index=False)
        
    if seatingcapacity:
        results = results[results['Seating Capacity'] <= seatingcapacity]
        results.to_csv('results2.csv', index=False)
        
    return render_template('results.html', tables=[results.to_html(classes='data table table-bordered table-hover table-sm')], titles=results.columns.values)


#*this is the home page
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/history')
def history():
    df = pd.read_csv('results2.csv')
    df.to_csv('results2.csv', index=False)
    return render_template("history.html", tables=[df.to_html(classes='data table table-bordered table-hover table-sm')], titles=df.columns.values)

@app.route('/home')
def home2():
    return render_template("index.html")

@app.route('/statistics')
def statistics():
    if selected_brand is None:
        return render_template("no_statistics.html")
    else:
        mean = ("Mean Price of " + selected_brand + " vehicles: "+str(MeanBrandPrice(df,selected_brand,2,'Mean')))
        median = ("Median Price of " + selected_brand + " vehicles: "+str(MeanBrandPrice(df,selected_brand,2,'Median')))
        mode = ("Mode Price of " + selected_brand + " vehicles: "+str(MeanBrandPrice(df,selected_brand,2,'Mode')))
        return render_template("statistics.html", mean=mean, median=median, mode=mode, selected_brand=selected_brand) 

# This function returns the data visualisation page
@app.route('/datavisualisation')
def data_visualisation():
    return render_template("data_visualisation.html")

# This function returns the about page
@app.route('/about')
def about():
    return render_template('about.html')

# This function returns the documentation page
@app.route('/documentation')
def documentation():
    return render_template('documentation.html')

# This function is used to search for a term
@app.route('/search', methods=['POST'])
def search():
    searched = request.form['searched']
    return render_template('search.html', searched=searched) 

# This function is used to clean data
@app.route('/clean_data', methods=['POST'])
def clean_data():
    df = cleandata(spreadsheet)
    print("CLEANED DATA")
    return render_template('clean.html')

# This function handles 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(TypeError)
def BrandNotDefined(e):
    return render_template('brandnotdefined.html')

@app.errorhandler(405)
def page_not_found(e):
    return render_template('405.html'), 405


if __name__ == "__main__":
    app.run(debug=True)
    print("search term: " + session['search'])
    






#*Instructions to run
#? export FLASK_APP=test_flask.py // or the directory of the file eg: 
#? flask run 
#? then go to http://127.0.0.1:5000 




