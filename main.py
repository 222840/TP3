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

    else : nombre_articles = 3

    return render_template("index.html",annee=annee,articles=articles,nombre_articles=nombre_articles)




@app.route("/construire/")
def construire():
    # TODO try catch

    return render_template("construire.html",annee=annee,choix_composantes=choix_composantes ,glossaire=glossaire )


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
    TAUX_taxes=0.15
    choix_case=request.form['case']
    choix_motherboard = request.form['motherboard']
    choix_cpu = request.form['cpu']
    choix_storage = request.form['storage']
    choix_cooling = request.form['cooling']
    choix_ram = request.form['ram']
    choix_power = request.form['power']
    choix_keyboard = request.form['keyboard']
    choix_mouse = request.form['mouse']
    choix_monitor = request.form['monitor']

    case=choix_composantes["case"][int(choix_case)-1].description
    prix_case=choix_composantes["case"][int(choix_case)-1].prix
    motherboard = choix_composantes["motherboard"][int(choix_motherboard)- 1].description
    prix_motherboard = choix_composantes["motherboard"][int(choix_motherboard) - 1].prix
    cpu = choix_composantes["cpu"][int(choix_cpu) - 1].description
    prix_cpu = choix_composantes["cpu"][int(choix_cpu) - 1].prix
    storage = choix_composantes["storage"][int(choix_storage) - 1].description
    prix_storage = choix_composantes["storage"][int(choix_storage) - 1].prix
    cooling = choix_composantes["cooling"][int(choix_cooling) - 1].description
    prix_cooling = choix_composantes["cooling"][int(choix_cooling) - 1].prix
    ram = choix_composantes["ram"][int(choix_ram) - 1].description
    prix_ram = choix_composantes["ram"][int(choix_ram) - 1].prix
    power = choix_composantes["power"][int(choix_power) - 1].description
    prix_power = choix_composantes["power"][int(choix_power) - 1].prix
    keyboard = choix_composantes["keyboard"][int(choix_keyboard) - 1].description
    prix_keyboard = choix_composantes["keyboard"][int(choix_keyboard) - 1].prix
    mouse = choix_composantes["mouse"][int(choix_mouse) - 1].description
    prix_mouse = choix_composantes["mouse"][int(choix_mouse) - 1].prix
    monitor = choix_composantes["monitor"][int(choix_monitor) - 1].description
    prix_monitor = choix_composantes["monitor"][int(choix_monitor) - 1].prix





    # remplis tableau avec les composantes de la page /construire/
    composante_de_ordinateur=[prix_case,prix_motherboard,prix_cpu+prix_storage,prix_cooling,prix_ram,prix_power,prix_keyboard,\
               prix_mouse,prix_monitor]

    #calcule le sous total mais ce n'est pas complet...
    panier=Ordinateur(composante_de_ordinateur)

    sous_total = round(panier.sous_total(),2)
    taxes = round(panier.taxes(),2)
    total = round(panier.total(),2)





    livraison=0 #initialisation du prix livraison


    # sous_total=prix_case+prix_motherboard+prix_cpu+prix_storage+prix_cooling+prix_ram+prix_power+prix_keyboard+\
    #            prix_mouse+prix_monitor;
    #
    # taxes=sous_total*TAUX_taxes
    #
    # total=sous_total+taxes+livraison



    return render_template("afficher-ordinateur.html",annee=annee,case=case,motherboard=motherboard,cpu=cpu,
            storage=storage,cooling=cooling,ram=ram,power=power,keyboard=keyboard,mouse=mouse,monitor=monitor,
                           sous_total=round(sous_total,2),taxes=round(taxes,2),total=round(total,2),livraison=round(livraison,2))



@app.route("/contact/")
def contact():
    # TODO try catch

    return render_template("contact.html",annee=annee)


if __name__ == "__main__":
    app.run(debug=True)

