from datetime import date, datetime, timedelta
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from functools import reduce
from time import strptime
import datetime as dt
import seaborn as sns
import pandas as pd
import numpy as np
import calendar
import swifter
import random
import json
import os

app = Flask(__name__)

#################################################
# Database Setup
#################################################

import pymongo
# Initialize PyMongo to work with MongoDBs
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
# Define database and collection
db = client.merged_data
merged_data = db.merged_data

@app.route("/")
def index():
    """Return the homepage."""
    merge_result = merged_data.find_one()
    if '_id' in merge_result:
        del merge_result['_id']
    return render_template("index.html", merge_data=merge_result)

    


if __name__ == "__main__":
    app.run()