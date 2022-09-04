from ordinaland import *
from flask import Flask,request,render_template
from django.core.paginator import Paginator,InvalidPage

import datetime
maintenent=datetime.datetime.now()
annee=maintenent.year

app = Flask(__name__)

if Article.numero <= 0:articles = [Article("Aucun article pour le moment","","","")]

@app.route("/")
def index():
    # TODO try catch
    if  Article.numero < 3:
        nombre_articles = len(articles)

    else: nombre_articles = 3

    return render_template("index.html",annee=annee,articles=articles,nombre_articles=nombre_articles)

@app.route("/construire/")
def construire():
    # TODO try catch



    return render_template("construire.html",annee=annee,choix_composantes=choix_composantes ,glossaire=glossaire,err=0, message=" " )

@app.route("/blog/<nb>")
def blog(nb):
    #TODO try catch
    tab_contenue=[]
    p=Paginator(articles,3)

    for i in articles:
        tab_contenue.append(i.tableau_paragraphes())

    try :
        page_active=p.page(nb)

    except (InvalidPage):
        page_active = p.page(1)

    return render_template("blog.html",p=p,articles=articles,page_active=page_active,annee=annee,)

@app.route("/article/<int:nb>")
def article(nb):
    # TODO try catch
    try:
        return render_template("article.html",articles=articles,nb=nb-1,annee=annee)
    except:
        nb=1
        return render_template("article.html", articles=articles, nb=nb - 1, annee=annee)


@app.route("/glossaire/")
def glossair():
    # TODO try catch

    return render_template("glossaire.html",annee=annee,glossaire=glossaire)


@app.route("/glossaire/<int:nb>")

def glossaire2(nb):

    return render_template("glossaire2.html", glossaire=glossaire, nb=nb, annee=annee)

    return render_template("glossaire.html",annee=annee)




@app.route("/afficher-ordinateur", methods=["POST"])
def afficher_ordinateur():
    # TODO try catch


    var_form_construire = {} #dicionnaire de variables récupérées dans la page : construire.html
    numero_index=[]

    message_erreur =""
    err = True
    for i,cle in enumerate(choix_composantes):
        numero_index.append(choix_composantes[cle])
        try :
            numero_index[i]=request.form[cle]
            var_form_construire[cle] = choix_composantes[cle][int(numero_index[i][0])]
            err = False

        except :
                message_erreur = "Votre panier est vide "



    codepostal = request.form['codepostal']
    livraison = calculerLivraison(codepostal)
    panier=Ordinateur(var_form_construire)

    sous_total = "{:.2f}".format(panier.sous_total())
    taxes = "{:.2f}".format(panier.taxes())
    total = "{:.2f}".format(panier.total())


    if livraison == True:
        err=True
        message_erreur = "Code postale invalide "

    if err ==True :
        return render_template("construire.html", annee=annee, choix_composantes=choix_composantes,
                               glossaire=glossaire, err=err, message_erreur=message_erreur)
    if len(var_form_construire) != 10:
        err=True



    return render_template("afficher-ordinateur.html",var_form_construire=var_form_construire,annee=annee,
                       sous_total=sous_total,taxes=taxes,total=float(total)+float(livraison),livraison=livraison,err=err)



def calculerLivraison(codepostal):
    codepostal = codepostal.replace(" ","")  # pour éliminer les espaces
    texte='ABCEGHJKLMNPRSTVXY'
    codepostal=codepostal.upper()
    print(codepostal)

    if (len(codepostal)==0):
        return 0

    elif (len(codepostal) !=6 ):
        return True

    elif (not codepostal[0] in texte)or(not codepostal[2].isalpha())or(not codepostal[4].isalpha())or\
        (not codepostal[1].isnumeric())or(not codepostal[3].isnumeric())or(not codepostal[5].isnumeric()):

        return True

    elif (codepostal[0] in "GHJ"):
        return 12.99;
    else:
        return 20.99;






@app.route("/contact/")
def contact():
    # TODO try catch

    return render_template("contact.html",annee=annee)


if __name__ == "__main__":
    app.run(debug=True)

