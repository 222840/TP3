#TP réalisé par Martin Bisson-Godbout et Siham Zaoui
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




#Chemin pour aller à la page construire un ordinateur
@app.route("/construire/")
def construire():

    return render_template("construire.html",annee=annee,choix_composantes=choix_composantes
                           ,glossaire=glossaire,err=0, message=" " )




#Chemin pour le panier des achats
@app.route("/afficher-ordinateur", methods=["POST"])
def afficher_ordinateur():
    dic_choix_form_construire_ordinateur = {}
    message_erreur =""
    erreur = True


    #Récupérer les choix de l'utilisateur et les mettrent dans un dictionnaire,
    # s'il y'a une erreur le message panier vide est affiché
    for i,cle in enumerate(choix_composantes):
        try :
            choix_du_client= request.form[cle]
            dic_choix_form_construire_ordinateur[cle] = choix_composantes[cle][int(choix_du_client)]
            erreur = False

        except :
                message_erreur = "Votre panier est vide "




    #Panier_du_client est un objet de classe Ordinateur qui va englober les choix du client
    panier_du_client=Ordinateur(dic_choix_form_construire_ordinateur)



    #récupère le code postal à partir de la forme puis calcule la livraison
    codepostal = request.form['codepostal']
    livraison = panier_du_client.calculer_livraison(codepostal)

    if livraison == True:
        erreur=True
        message_erreur = "Code postale invalide "

    if erreur ==True :
        return render_template("construire.html", annee=annee, choix_composantes=choix_composantes,
                               glossaire=glossaire, err=erreur, message_erreur=message_erreur)

    if len(dic_choix_form_construire_ordinateur) != 10:
        erreur=True

    sous_total = "{:.2f}".format(panier_du_client.sous_total())
    taxes = "{:.2f}".format(panier_du_client.taxes())
    total = "{:.2f}".format(panier_du_client.total()+(livraison))

    return render_template("afficher-ordinateur.html",var_form_construire=dic_choix_form_construire_ordinateur,annee=annee,
                       sous_total=sous_total,taxes=taxes,total=total,livraison=livraison,err=erreur)




if Article.numero <= 0:articles = [Article("Aucun article pour le moment","","","")]
@app.route("/blog/<nb>")
def blog(nb):
    p=Paginator(articles,3)

    try :
        page_active=p.page(nb)

    except (InvalidPage):
        page_active = p.page(1)

    return render_template("blog.html",p=p,articles=articles,page_active=page_active,annee=annee,)




@app.route("/article/<int:nb>")
def article(nb):

    try:
        return render_template("article.html",articles=articles,nb=nb-1,annee=annee)

    except:
        nb=1
        return render_template("article.html", articles=articles, nb=nb - 1, annee=annee)




#Chemin pour la page principal de glossaire
@app.route("/glossaire/")
def glossair():
    return render_template("glossaire.html",annee=annee,glossaire=glossaire)




#Chemin pour les différentes composantes du glossaire
@app.route("/glossaire/<int:nb>")
#glossaire2.html est la 2ème page web pour les différentes composantes du glossaire
def glossaire2(nb):
    try:
        return render_template("glossaire2.html", glossaire=glossaire, nb=nb, annee=annee)
    except :
        return render_template("glossaire.html",annee=annee,glossaire=glossaire)




#Chemin pour la page contact
@app.route("/contact/")
def contact():
    return render_template("contact.html",annee=annee)


if __name__ == "__main__":
    app.run(debug=True)
