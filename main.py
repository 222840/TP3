from ordinaland import *
from flask import Flask,request,render_template
from django.core.paginator import Paginator

import datetime
maintenent=datetime.datetime.now()
annee=maintenent.year

app = Flask(__name__)


#test
@app.route("/")
def index():
    # TODO try catch  {% for i  in range (0,3)  %}


    return render_template("index.html",annee=annee,articles=articles)

@app.route("/construire/")
def construire():
    # TODO try catch

    return render_template("construire.html",annee=annee)

@app.route("/blog/<int:nb>")
def blog(nb):
    #TODO try catch
    tab_contenue=[]
    p=Paginator(articles,3)

    for i in articles:
        tab_contenue.append(i.tableau_paragraphes())

    page_active=p.page(nb)

    return render_template("blog.html",p=p,articles=articles,page_active=page_active,annee=annee)


@app.route("/article/<int:nb>")
def article(nb):
    # TODO try catch


    return render_template("article.html",articles=articles,nb=nb-1,annee=annee)


@app.route("/glossaire/")
def glossaire():
    # TODO try catch

    return render_template("glossaire.html",annee=annee)

@app.route("/contact/")
def contact():
    # TODO try catch

    return render_template("contact.html",annee=annee)


if __name__ == "__main__":
    app.run(debug=True)