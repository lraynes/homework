import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the tables
Measurement = Base.classes.measurements
Station = Base.classes.stations

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

app = Flask(__name__)

@app.route("/api/v1.0/precipitation")
def precipitation():
    results = session.query(Measurement).\
        filter(Measurement.prcp != "None").all()

    rain_data = []
    for observation in results:
        rain_dict = {}
        rain_dict["date"] = observation.date
        rain_dict["prcp"] = observation.prcp
        rain_data.append(rain_dict)
        
    return jsonify(rain_data)

@app.route("/api/v1.0/stations")
def stations():
    
    results = session.query(Station).all()

    stations = []
    for observation in results:
        stations.append(observation.station)
      
    return jsonify(stations)

@app.route("/api/v1.0/tobs")
def tobs():
    year_ago = dt.date(2017,8,23) - dt.timedelta(days=365)

    results = session.query(Measurement.tobs).\
        filter(Measurement.tobs != "None").\
        filter(Measurement.date >= year_ago).all()
    
    tobs = []
    for observation in results:
        tobs.append(observation.tobs)

    return jsonify(tobs)

@app.route("/api/v1.0/<start>")
def start_date(start):
    start_convert = start.split("-")
        
    search = dt.date(int(start_convert[0]), int(start_convert[1]), int(start_convert[2]))

    results = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.tobs != "None").\
        filter(Measurement.date >= search).all()

    temps = []

    #Checks if date is after the time periods recorded
    if not results:
        return jsonify({"error": f"The date {start} was not found."}), 404
    #Checks if date is before time periods recorded
    elif start != results[0][0]:
        return jsonify({"error": f"The date {start} was not found."}), 404
    else:
        for observation in results:
            temps.append(int(observation.tobs))
        
        temps_dict = {}
        temps_dict["minimum temperature"] = min(temps)
        temps_dict["maximum temperature"] = max(temps)
        temps_dict["average temperature"] = round(np.mean(temps),2)

        return jsonify(temps_dict)

@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    start_convert = start.split("-")
    end_convert = end.split("-")
        
    search_start = dt.date(int(start_convert[0]), int(start_convert[1]), int(start_convert[2]))
    search_end = dt.date(int(end_convert[0]), int(end_convert[1]), int(end_convert[2]))

    results = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.tobs != "None").\
        filter(Measurement.date >= search_start, Measurement.date <= search_end,).all()

    temps = []

    #Checks if date is after the time periods recorded
    if not results:
        return jsonify({"error": f"The date {start} was not found."}), 404
    #Checks if date is before time periods recorded
    elif start != results[0][0]:
        return jsonify({"error": f"The date {start} was not found."}), 404
    elif end != results[-1][0]:
        return jsonify({"error": f"The date {end} was not found."}), 404
    else:
        for observation in results:
            temps.append(int(observation.tobs))
        
        temps_dict = {}
        temps_dict["minimum temperature"] = min(temps)
        temps_dict["maximum temperature"] = max(temps)
        temps_dict["average temperature"] = round(np.mean(temps),2)

        return jsonify(temps_dict)    
    



if __name__ == "__main__":
    app.run(debug=True)