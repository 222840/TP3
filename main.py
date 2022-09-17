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





@app.route("/construire/")
def construire():
    """
    Chemin pour page construire un ordinateur
    :return:construire.html
    """

    return render_template("construire.html",annee=annee,choix_composantes=choix_composantes
                           ,glossaire=glossaire,err=0, message=" " )





@app.route("/afficher-ordinateur", methods=["POST"])
def afficher_ordinateur():
    """
    Chemin pour page résultat de la construction d'un ordinateur
    :return: afficher-ordinateur.html
    """
    dic_choix_form_construire_ordinateur = {}
    message_erreur =""
    erreur = True


    # Récupérer les choix de l'utilisateur et les mettrent dans un dictionnaire,
    # s'il y'a une erreur le message panier vide est affiché
    for i,cle in enumerate(choix_composantes):
        try :
            choix_du_client= request.form[cle]
            dic_choix_form_construire_ordinateur[cle] = choix_composantes[cle][int(choix_du_client)]
            erreur = False

        except :
                message_erreur = "Votre panier est vide "




    # Panier_du_client est un objet de classe Ordinateur qui va englober les choix du client
    panier_du_client=Ordinateur(dic_choix_form_construire_ordinateur)



    # Récupère le code postal à partir de la forme puis calculer la livraison
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

    sous_total = "{:.2f}".format(panier_du_client.calcule_sous_total())
    taxes = "{:.2f}".format(panier_du_client.calcule_taxes())
    total = "{:.2f}".format(panier_du_client.calcul_total() + (livraison))

    return render_template("afficher-ordinateur.html",var_form_construire=dic_choix_form_construire_ordinateur,annee=annee,
                       sous_total=sous_total,taxes=taxes,total=total,livraison=livraison,err=erreur)




if Article.numero <= 0:articles = [Article("Aucun article pour le moment","","","")]
@app.route("/blog/<nb>")
def blog(nb):
    """
    Chemin page /blog/
    :param nb: numéro de la pagination
    :return: blog.html
    """
    p=Paginator(articles,3)

    try :
        page_active=p.page(nb)

    except (InvalidPage):
        page_active = p.page(1)

    return render_template("blog.html",p=p,articles=articles,page_active=page_active,annee=annee,)




@app.route("/article/<int:nb>")
def article(nb):
    """
    Chemin page /article/
    :param nb:numéro de l'article
    :return:article.html
    """

    try:
        return render_template("article.html",articles=articles,nb=nb-1,annee=annee)

    except:
        nb=1
        return render_template("article.html", articles=articles, nb=nb - 1, annee=annee)





@app.route("/glossaire/")
def glossair():
    """
    Chemin pour la page principal de glossaire
    :return: glossaire.html
    """
    return render_template("glossaire.html",annee=annee,glossaire=glossaire)





@app.route("/glossaire/<int:nb>")
#
def glossaire2(nb):
    """
    Chemin pour les différentes composantes du glossaire
    :param nb: numéro des différentes composantes du glossaire
    :return: glossaire2.html
    """
    try:
        return render_template("glossaire2.html", glossaire=glossaire, nb=nb, annee=annee)
    except :
        return render_template("glossaire.html",annee=annee,glossaire=glossaire)





@app.route("/contact/")
def contact():
    """
    Chemin pour la page contact
    :return: contact.html
    """
    return render_template("contact.html",annee=annee)


if __name__ == "__main__":
    app.run(debug=True)
