'''

Written by alfredc333
'''

import os
import time

from flask import (
    Flask,
    g,
    jsonify,
    make_response,
)

from . import db

path = os.path.abspath(".")
instancePath = os.path.join(path, '../instance')  
print(instancePath)

app = Flask(__name__, instance_path=instancePath)
print(app.instance_path)

app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'sensorData.db'),
    )

db.init_db_app(app)

@app.route("/")
def hello_world():
    return "<p>Flask is up and running.</p>"


@app.route("/getData")
def getData():
    ts = time.strftime("%Y-%m-%d %H:%M:%S")
    app.logger.debug('Starting DB retrieval at ' + ts)
    dbH = db.get_db()
    query = 'SELECT * from Measurements ORDER By Mid DESC'
    cur = dbH.execute(query)
    rows = cur.fetchone()

    response = make_response(
        jsonify({
            'Mid': str(rows["Mid"]),
            'Temperature': str(rows["Temperature"]),
            'Humidity': str(rows["Humidity"]),
            'AirPressure': str(rows["AirPressure"]),
            'CO2level': str(rows["CO2level"]),
            'Measurement Timestamp': str(rows["Timestamp"]),
            'Real time Timestamp': ts
        }), 200)

    response.headers["Content-Type"] = "application/json"
    return response

