from flask import Flask, render_template
from data import *

app = Flask(__name__)


@app.route('/')
def render_main_page():
    return render_template('index.html', departures=departures, tours=tours)


@app.route('/departures/<departure>/')
def render_departures_page(departure):
    return render_template('departure.html', departures=departures, departure=departure, tours=tours)


# @app.route('/tours/<id>/')
# def render_tours_page(id):
#     return render_template('tour.html', departures=departures)


app.run('0.0.0.0', 8000)
