from ordinaland import *
from flask import Flask,request,render_template
import datetime
maintenent=datetime.datetime.now()
annee=maintenent.year

app = Flask(__name__)

@app.route("/")
def index():

    return render_template("index.html",annee=annee,titre1=articles[0].titre,texte1=articles[0].texte,
                           titre2=articles[1].titre,texte2=articles[1].texte,titre3=articles[2].titre,texte3=articles[2].texte)

@app.route("/construire/")
def construire():

    return render_template("construire.html",annee=annee)

@app.route("/blog/")
def blog():
    nb=1
    article_de_la_page=[articles[nb].texte,articles[nb+1].texte,articles[nb+2].texte]
    return render_template("blog.html",annee=annee,nb_page=Article.pagination()[0],modulo=Article.pagination()[1],article_de_la_page=article_de_la_page,nb=nb)

@app.route("/glossaire/")
def glossaire():

    return render_template("glossaire.html",annee=annee)

@app.route("/contact/")
def contact():

    return render_template("contact.html",annee=annee)


if __name__ == "__main__":
    app.run(debug=True)