from ordinaland import *
from flask import Flask,request,render_template
import datetime
maintenent=datetime.datetime.day


app = Flask(__name__)

@app.route("/")
def index():

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)