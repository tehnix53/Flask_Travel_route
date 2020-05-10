from flask import Flask, render_template
import requests
from data import *

app = Flask(__name__)


@app.route('/tour/<id>/')
def tour_sample(id):
    return render_template('tour.html', departures=departures, title=title, tours_list=tours_list)


@app.route('/')
def stepic_index():
    return render_template('index.html', title=title, subtitle=subtitle, description=description, \
                           departures=departures, tours=tours, tours_list=tours_list)


@app.route('/departure/<id>/')
def thirst(id):
    filtered = ([i for i in tours_list if ('/departure/' + str(i["departure"]) + '/') == '/departure/' + id + '/'])
    price = [i['price'] for i in filtered]
    nights = [i['nights'] for i in filtered]
    return render_template('departure.html', departures=departures, title=title, tours_list=tours_list,
                           filtered=filtered, price=price, nights=nights)


app.run('127.0.0.1', 8000, debug=True)
