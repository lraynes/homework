import pymongo
from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of our Flask app.
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/marsDB"
mongo = PyMongo(app)


# Set route
@app.route('/')
def index():
    
    marsDB = mongo.db.marsDB.find_one()
    return render_template("index.html", marsDB=marsDB)



@app.route("/scrape")
def scraper():

    marsDB = mongo.db.marsDB
    mars_data = scrape_mars.scrape()
    marsDB.update(
        {},
        mars_data,
        upsert=True
    )
    return redirect("http://localhost:5000/", code=302)



if __name__ == "__main__":
    app.run(debug=True)