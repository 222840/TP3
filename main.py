from ordinaland import *
from flask import Flask,request,render_template
import datetime
maintenent=datetime.datetime.day


app = Flask(__name__)

@app.route("/")
def index():

    return render_template("index.html")

@app.route("/construire/")
def construire():

    return render_template("construire.html")

@app.route("/blog/")
def blog():

    return render_template("blog.html")

@app.route("/glossaire/")
def glossaire():

    return render_template("glossaire.html")

@app.route("/contact/")
def contact():

    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)