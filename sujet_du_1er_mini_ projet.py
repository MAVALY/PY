from collections import Counter
import pandas
from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse


######################## ETAPE 1 #########################

def etape_1(texte):
    variable_1 = texte.split()
    variable_2 = Counter(variable_1)

    variable_final = dict(sorted(variable_2.items(), key=lambda item: item[1], reverse=True))

    return variable_final

texte = "Je suis MAVALY Kameshdassane c'est un test pour le code ceci est un test."
resultat = etape_1(texte)

print("Liste de mots avec occurence", resultat)

######################## ETAPE 2 #########################

def etape_2(donnees, mots_parasites):
    variable_3= {mot: occurrence for mot, occurrence in donnees.items() if mot not in mots_parasites}
    return variable_3

mots_parasites = ['le', 'la', 'les', 'un', 'une', 'pour','ce', 'de', 'des']

retour_sans_les_parasites = etape_2(resultat, mots_parasicleates)

print("Sans les parasites", retour_sans_les_parasites)

######################## ETAPE 3 #########################

def etape_3(nom_fichier):
    try:
        parasites = pandas.read_csv("parasite.csv")
    except:
        print("Fichier introuvable.")

    return parasites



fichier_csv = 'C:\Users\Kamesh\Documents'  # Remplacez ceci par le chemin vers votre fichier CSV
liste_mots_parasites = etape_3(fichier_csv)

print(liste_mots_parasites)

######################## ETAPE 5 #########################

def etape_5(html):
    variable_4 = BeautifulSoup(html, 'html.parser')
    texte_sans_balises = variable_4.get_text(separator=' ', strip=True)
    return texte_sans_balises

# Exemple d'utilisation
html_texte = "<p>Ceci est un <b>exemple</b> de texte HTML.</p><a href='#'>Un lien</a>"
texte_sans_balises = etape_5(html_texte)

print("Texte sans balises HTML:", texte_sans_balises)

######################## ETAPE 6 & 7 #########################

def extraire_valeurs_attribut(html, nom_balise, nom_attribut):
    valeurs = []

    variable_6 = BeautifulSoup(html, 'html.parser')
    balises = variable_6.find_all(nom_balise)

    for balise in balises:
        valeur_attribut = balise.get(nom_attribut)
        if valeur_attribut:
            valeurs.append(valeur_attribut)

    return valeurs

######################## ETAPE 8 #########################

def etape_8(url):
    nom_domaine = urlparse(url).netloc
    print(nom_domaine)


url_test = 'https://esiee-it.blackboard.com/ultra/'
test_html = etape_8(url_test)

######################## ETAPE 9 #########################

def filtrer_urls_par_domaine(nom_domaine, liste_urls):
    urls_partie_domaine = []
    urls_pas_partie_domaine = []

    for url in liste_urls:
        variable_7 = urlparse(url)
        variable_8 = variable_7.netloc

        if variable_8 == nom_domaine:
            urls_partie_domaine.append(url)
        else:
            urls_pas_partie_domaine.append(url)

    return urls_partie_domaine, urls_pas_partie_domaine

# Exemple d'utilisation
nom_domaine = "esiee-it.blackboard.com"
urls = ["https://esiee-it.blackboard.com/ultra/kam", "https://esiee-it.blackboard.com/ultra/global "]

urls_dans_domaine, urls_hors_domaine = filtrer_urls_par_domaine(nom_domaine, urls)

print(f"URLs dans le domaine '{nom_domaine}': {urls}")
print(f"URLs hors du domaine '{nom_domaine}': {urls}")

######################## ETAPE 10 #########################




