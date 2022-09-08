from ordinaland import *
from flask import Flask,request,render_template
from django.core.paginator import Paginator,InvalidPage

import datetime
maintenent=datetime.datetime.now()
annee=maintenent.year

app = Flask(__name__)



@app.route("/")
def index():
    if  Article.numero < 3:
        nombre_articles = len(articles)
    else: nombre_articles = 3

    return render_template("index.html",annee=annee,articles=articles,nombre_articles=nombre_articles)



@app.route("/construire/")
def construire():

    compteur=0
    for cle in choix_composantes.keys():
        print(cle,glossaire[compteur].source)
        compteur += 1
        for i in range (len(choix_composantes[cle])):
            print(choix_composantes[cle][i].description,choix_composantes[cle][i].prix)


    # for i in range(len(glossaire)):
    #     print(glossaire[i].terme)
    #     for y in range (len(choix_composantes[str(glossaire[i].terme)])):
    #         print(choix_composantes[str(glossaire[i].terme)][y].description)

    return render_template("construire.html",annee=annee,choix_composantes=choix_composantes ,glossaire=glossaire,err=0, message=" " )




@app.route("/afficher-ordinateur", methods=["POST"])
def afficher_ordinateur():
    var_form_construire = {} #dicionnaire de variables récupérées dans la page : construire.html
    message_erreur =""
    erreur = True

    numero_index = []
    for i,cle in enumerate(choix_composantes):
        numero_index.append(choix_composantes[cle])
        try :
            numero_index[i]=request.form[cle]
            var_form_construire[cle] = choix_composantes[cle][int(numero_index[i][0])]
            erreur = False

        except :
                message_erreur = "Votre panier est vide "


    codepostal = request.form['codepostal']
    panier=Ordinateur(var_form_construire)

    livraison = panier.calculer_livraison(codepostal)

    if livraison == True:
        erreur=True
        message_erreur = "Code postale invalide "

    if erreur ==True :
        return render_template("construire.html", annee=annee, choix_composantes=choix_composantes,
                               glossaire=glossaire, err=erreur, message_erreur=message_erreur)
    if len(var_form_construire) != 10:
        erreur=True

    sous_total = "{:.2f}".format(panier.sous_total())
    taxes = "{:.2f}".format(panier.taxes())
    total = "{:.2f}".format(panier.total()+(livraison))

    return render_template("afficher-ordinateur.html",var_form_construire=var_form_construire,annee=annee,
                       sous_total=sous_total,taxes=taxes,total=total,livraison=livraison,err=erreur)




if Article.numero <= 0:articles = [Article("Aucun article pour le moment","","","")]
@app.route("/blog/<nb>")
def blog(nb):
    tab_contenue=[]
    p=Paginator(articles,3)

    for i in articles:
        tab_contenue.append(i.tableau_paragraphes())

    try :
        page_active=p.page(nb)

    except (InvalidPage):
        page_active = p.page(1)
    #print(page_active.next_page_number())
    #print(page_active.previous_page_number())
    #print(page_active.has_previous())
    return render_template("blog.html",p=p,articles=articles,page_active=page_active,annee=annee,)




@app.route("/article/<int:nb>")
def article(nb):
    try:
        return render_template("article.html",articles=articles,nb=nb-1,annee=annee)
    except:
        nb=1
        return render_template("article.html", articles=articles, nb=nb - 1, annee=annee)


@app.route("/glossaire/")
def glossair():
    return render_template("glossaire.html",annee=annee,glossaire=glossaire)


@app.route("/glossaire/<int:nb>")

def glossaire2(nb):
    try:
        return render_template("glossaire2.html", glossaire=glossaire, nb=nb, annee=annee)

    except :

        return render_template("glossaire.html",annee=annee,glossaire=glossaire)




@app.route("/contact/")
def contact():

    return render_template("contact.html",annee=annee)


if __name__ == "__main__":
    app.run(debug=True)

