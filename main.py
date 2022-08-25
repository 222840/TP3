from ordinaland import *
from flask import Flask,request,render_template
from django.core.paginator import Paginator

import datetime
maintenent=datetime.datetime.now()
annee=maintenent.year

app = Flask(__name__)

@app.route("/")
def index():
    # TODO try catch

    return render_template("index.html",annee=annee,titre1=articles[0].titre,texte1=articles[0].texte,
                           titre2=articles[1].titre,texte2=articles[1].texte,titre3=articles[2].titre,texte3=articles[2].texte)

@app.route("/construire/")
def construire():
    # TODO try catch

    return render_template("construire.html",annee=annee)

@app.route("/blog/<int:nb>")
def blog(nb):
    #TODO try catch
    tab_contenue=[]
    p=Paginator(tab_contenue,3)

    for i in articles:
        tab_contenue.append(i.get_texte())
    page_active=p.page(nb)

    if page_active.has_previous():
        page_precedente = page_active.previous_page_number()
    else:page_precedente = page_active.start_index()

    if page_active.has_next():
        page_suivante = page_active.next_page_number()
    else: page_suivante=p.num_pages

    return render_template("blog.html",p=p,articles=articles,page_active=page_active,page_precedente=page_precedente,page_suivante=page_suivante,annee=annee)

def blog(nb):
    # TODO try catch
    tab_contenue=[]
    p=Paginator(tab_contenue,3)

    for i in articles:
        tab_contenue.append(i.get_texte())
    page_active=p.page(nb)

    if page_active.has_previous():
        page_precedente = page_active.previous_page_number()
    else:
        page_precedente = page_active.start_index()

    if page_active.has_next():
        page_suivante = page_active.next_page_number()
    else:
        page_suivante = page_active.end_index()
    print(page_active)
    print(page_suivante)
    print(page_precedente)
    print(p.num_pages)
    print(len(tab_contenue))
    for i in page_active.object_list:
        print(i)
blog(5)



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