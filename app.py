# Module 9.5.1 Set Up the Database and Flask
## Set Up the Flask Weather App
# import our dependencies to our code environment, import is datetime, NumPy, and Pandas...
# assign each of these an alias
import datetime as dt
import numpy as np
import pandas as pd

# get the dependencies we need for SQLAlchemy, which will help us access our data in the SQLite database
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# code to import the dependencies that we need for Flask. You'll import these right after your SQLAlchemy dependencies
from flask import Flask, jsonify

# Set Up the Database
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect the database into our classes.
Base = automap_base()

# reflect the database:
Base.prepare(engine, reflect=True)

# save our references to each table, create a variable for each of the classes so that we can reference them later
Measurement = Base.classes.measurement
Station = Base.classes.station

# create a session link from Python to our database
session = Session(engine)

# Set Up Flask
# define our app for our Flask application, the __name__ variable is a special type of variable
app = Flask(__name__)

# Module 9.5.2 Create the Welcome Route
#IMPORTANT
#All of your routes should go after the app = Flask(__name__) line of code. Otherwise, your code may not run properly.
# define the welcome route using the code below
@app.route("/")

# add the routing information for each of the other routes. create a function, and our return statement will have f-strings as a reference to all of the other routes.
# create a function welcome() with a return statement
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

#note : When creating routes, we follow the naming convention /api/v1.0/ followed by the name of the route
# run Flask applications by using the command flask run in your navigation folder

# Module 9.5.3 Precipitation Route
# CAUTION : Every time you create a new route, your code should be aligned to the left in order to avoid errors.
# To create the route, add the following code. Make sure that it's aligned all the way to the left.
@app.route("/api/v1.0/precipitation")

# create the precipitation() function.
# create a dictionary with the date as the key and the precipitation as the value
# "jsonify" our dictionary. Jsonify() is a function that converts the dictionary to a JSON file
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

# Module 9.5.4 9.5.4 Stations Route
# return a list of all the stations, begin by defining the route and route name
@app.route("/api/v1.0/stations")

# create a new function called stations(), create a query that will allow us to get all of the stations in our database
# convert our unraveled results into a list. To convert the results to a list, we will need to use the list function, which is list(), and then convert that array into a list
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

# Module 9.5.5 Monthly Temperature Route
# return the temperature observations for the previous year
@app.route("/api/v1.0/tobs")

# create a function called temp_monthly(), calculate the date one year ago, query the primary station, one-dimensional array and convert that array into a list, jsonify our temps list
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

# Module 9.5.6 Statistics Route
# report on the minimum, average, and maximum temperatures
# create the routes
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

# create a function called stats() with a start parameter and an end parameter
# create a query to select the minimum, average, and maximum temperatures from our SQLite database
# to determine the starting and ending date, add an if-not statement 
# jsonify our results and return
# calculate the temperature minimum, average, and maximum with the start and end dates. We'll use the sel list, which is simply the data points we need to collect
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)




