from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def render_main_page():
    return render_template('index.html')


@app.route('/departures/<departure>/')
def render_departures_page(departure):
    return render_template('departure.html')


@app.route('/tours/<id>/')
def render_tours_page(id):
    return render_template('tour.html')


app.run('0.0.0.0', 8000)
