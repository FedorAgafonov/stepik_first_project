from flask import Flask, render_template
from data import departures
from data import tours
from data import title

app = Flask(__name__)


@app.route('/')
def render_main_page():
    tour = {}
    for k, v in tours.items():
        if len(tour) == 6:
            break
        tour[k] = v
    return render_template('index.html', title=title, departures=departures, tours=tour)


@app.route('/departures/<departure>/')
def render_departures_page(departure):
    tour = {}
    for key, value in tours.items():
        if value['departure'] == departure:
            tour[key] = value
    min_p = 1000000
    max_p = 0
    min_n = 100
    max_n = 0
    for val in tour.values():
        if val['price'] < min_p:
            min_p = val['price']
        if val['price'] > max_p:
            max_p = val['price']
        if val['nights'] < min_n:
            min_n = val['nights']
        if val['nights'] > max_n:
            max_n = val['nights']
    return render_template('departure.html', title=title, departures=departures, departure=departure, tours=tour, min_p=min_p, max_p=max_p, min_n=min_n, max_n=max_n)


@app.route('/tours/<int:id>/')
def render_tours_page(id):
    return render_template('tour.html', title=title, departures=departures, data_for_tour=tours[id])


app.run('0.0.0.0', 8000)
