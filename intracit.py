from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import datetime
import cgitb
import sys

app = Flask(__name__)
Bootstrap(app)
cgitb.enable()
sys.path.insert(0, "/usr/bin/espeak")


@app.route("/")
def hello():
    now = datetime.datetime.now()
    timestring = now.strftime("%Y-%m-%d %H:%M")
    templatedata = {
        'title': 'We',
        'time': timestring}

    return render_template('main.html', **templatedata)


@app.route("/test/")
def sup():

    return render_template('index.html')


@app.route("/gmapstest/")
def gsup():

    return render_template('gmaps_test.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
