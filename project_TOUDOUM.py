# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt # Importation de Matplotlib <3

######################  Importation du tableau  ##############################
tableau = [] # Crée une liste
with open("netflix.csv", "r", encoding="UTF-8") as fichier : #Ouvre le fichier contenant les données
    cles = fichier.readline()[:-1].split(";") # lit la ligne
    for ligne in fichier : # Conversion d'une ligne en dictionnaire
        valeurs = ligne[:-1].split(";")
        dico = dict()
        for cle, valeur in zip(cles, valeurs) :
            dico[cle] = valeur
        tableau.append(dico)
# show_id;type;title;director;cast;country;date_added;release_year;rating;duration;listed_in;description     Descripteur
##############################################################################




##################################  Type  ####################################

"""entry = [l["type"] for l in tableau]
x = list(set(entry))
x.pop(index("")) # bye bye Memphis belle
y = [0 for i in range(len(x))]
for i in tableau:
    for j in range(len(x)):
        if (i["type"] == x[j]) :
            y[j] += 1"""

######## Code plus optimisé mais pas "adaptatif" :
"""
  Le principe *général* :
  |           .
  |     . .  .
y |   .    .
  |___________
        x
"""
x = ["TV Show", "Movie"]
y = [0, 0]
for i in tableau: # Ajoute +1 si c'est un film ou un show télé'
    if (i["type"] == "TV Show"):
        y[0] += 1
    else :
        y[1] += 1

plt.bar(range(2), y, zorder=5.0)                 # Diagramme à barres / Graphique en barres (zorder c'est pour le placer devant la grille (d'où le Z pour l'axe))
plt.grid(zorder=0)                               # Grille
plt.xticks(range(2), ["Show télévisé", "Film"])  # Ajoute les étiquettes sur l'axe des X
plt.title("Type de programme")                   # Titre du graphique
plt.show()                                       # Montre le graphique
plt.close()                                      # Ferme Matplotlib

##############################################################################




###########################  Tableau des temps  #############################
### Enlever l'élément buggé   The Memphis Belle: A Story of a ...
id_ = 0
for i in range (len(tableau)) :
	if (tableau[i]["show_id"] == "80119194") :
		id_ = i
tableau.pop(id_)

time = []                         # Créer une liste vide Temps
for l in tableau  :               # Regarde pour chacun des éléments si ...
    if (l["type"] == "Movie"):    # ... le "type" est bien celui d'un film
        n = l["duration"]         # Prend sa durée
        n = n[0:len(n)-4]         # Enlève " min" de la chaîne de caractères
        time.append(int(n))       # Ajoute la durée convertie à la liste
###############################################################################




#############################  Total de films  ################################
i=0
for l in tableau: # Ajoute +1 pour chaque élément étant un film
    if (l["type"]=="Movie"):
        i+=1
print("Il y a", i, "films sur Netflix")
###############################################################################




#########################  CONVERTION DUREE  ##################################
for l in tableau :                                                   # Pareil que pour la liste Temps (time) mais là on convertit la liste d'origine
    if (l["type"] == "Movie"):                                       # Si c'est un film
        l["duration"] = int(l["duration"][0:len(l["duration"])-4])   # Change la durée stockée (chaîne de caractère avec " min") en nombre entier utilisable
###############################################################################




#########################   DUREE  ############################################
maxi = 0                              # Durée max
id_maxi = ""                          # le film ayant cette durée
mini = 300                            # Durée minimum
id_mini = ""                          # le film ayant cette durée
for l in tableau:                     # Regarde pour chaque éléments si ...
    if (l["type"] == "Movie"):        # ... c'est un film et si ...
        if (l["duration"] > maxi):    # ... il bat le record Max ...
            maxi = l["duration"]            # change le record
            id_maxi = l
        if (l["duration"] < mini):    # ... ou le record Minimum
            mini = l["duration"]            # change le record
            id_mini = l

# Afdiche les résultats
print("Plus court film :", id_mini["title"], "avec seulement", mini, " minutes")
print("Plus long film :",  id_maxi["title"], "avec",           maxi, " minutes")
###############################################################################




########################  FUNCTION SEARCH  ####################################
def search(list_, element, retour): # PAS UTILISÉE :)
    """
        FONCTION PRMETTANT DE RECHERCHER UN ELEMENT PRECIS
        DANS UNE LISTE DONNE. ELLE RETOURNE UNE LISTE DES
        ELEMENTS TROUVES CORRESPONDANTS
    """
    result = [ligne for ligne in list_ if(eval(element))]
    if (retour != ""):
        return eval(retour)
    else :
        return result
###############################################################################




#######################  TABLEAU DUREE FILMS  #################################
x = list(set(time)) # Liste des différents durées possibles
y = [0 for i in x]  # Liste remplie de 0 et de longueur identique à x
for l in time :     # Ajoute +1 pour chaque durées trouvées dans le tableau de données des temps
    y[x.index(l)] += 1

### Fonction pour graphique simple
def simplePlot(_x, _y, _title, _ylabel, _xlabel, _rotation, _grid) :
	plt.plot(_x, _y)                       # Graphique
	plt.title(_title)                      # Titre
	plt.ylabel(_ylabel)                    # Titre axe des Y
	plt.xlabel(_xlabel)                    # Titre axe des X
	if (_grid == True):                    # Grille
		plt.grid()
	plt.xticks(rotation=_rotation)         # Rotation
	plt.show()                             # Affiche
	plt.close()                            # Ferme Matplotlib

simplePlot(x, y, "Nombre de films par durée", "Nombre de films", "Durées", 0, False)
###############################################################################




######################### Temps : Max et Min Date  ############################
yearMax = 0 # Max Année
monthMax= 0 # Max Mois
dayMax  = 0 # Max Jour

yearMin = 3000 # Minimum Année
monthMin= 3000 # Minimum Mois
dayMin  = 3000 # Minimum Jour

# Aide à la division d'une date en indice d'array :
# 2 2 / 0 9 / 2 0 1 7
# 0 1 2 3 4 5 6 7 8 9

for l in tableau : # pour chaque éléments du tableau :
    if (l["date_added"] != "" and l["date_added"] != "00/00/0000"): # Si la date est valide :
        #print(l["date_added"][6:10], l["date_added"][3:5], l["date_added"][0:2])          # DEBUG
        y = int(l["date_added"][6:10]) # Créer la variable temporaire de l'année
        m = int(l["date_added"][3:5])  # Créer la variable temporaire du mois
        d = int(l["date_added"][0:2])  # Créer la variable temporaire du jour

        recordMax = False                                                    # Variable si le record est battue
        if (y > yearMax) : recordMax = True                                  # record battue ?
        if (m > monthMax and y >= yearMax) : recordMax = True                # record battue ?
        if (d > dayMax and m >= monthMax and y > yearMax) : recordMax = True # record battue ?

        if (recordMax == True) : # Si le record a été battue alors il faut actualiser les records
            yearMax = y
            monthMax= m
            dayMax  = d

        recordMin = False                                                    # Variable si le record est battue
        if (y < yearMin) : recordMin = True                                  # record battue ?
        if (m < monthMin and y <= yearMin) : recordMin = True                # record battue ?
        if (d < dayMin and m <= monthMin and y < yearMin) : recordMin = True # record battue ?

        if (recordMin == True) : # Si le record a été battue alors il faut actualiser les records
            yearMin = y
            monthMin= m
            dayMin  = d

# Affiche les résultats
print("Premier film ajouté :", dayMax, "/", monthMax, "/", yearMax)
print("Dernier film ajouté :", dayMin, "/", monthMin, "/", yearMin)
###############################################################################




###################################  Genres  ##################################
listType = [l["listed_in"].split(",") for l in tableau if (l["listed_in"] != "")] # Liste de toutes les listes genres
allList = [] # Crée une liste vide
y = []       # Crée une liste vide
for l in listType :                  # Pour tout les liste de genres récupérés ...
    for i in l :                     # Regarder pour tout les genres dans ces listes de genres ...
        i = i.strip()                # Enlève les espaces
        if (i in allList) :          # Si le genre examiné est dans la liste ...
            y[allList.index(i)] += 1 # Ajoute +1 à au nombre de ce genre trouvé
        else:                        # Sinon
            allList.append(i)        # Ajoute le genre à la liste
            y.append(1)              # not 0 because it has to be found to be added to the list
print("There are",len(allList),"different show categories")

### -> Partie rangement
def sortList(list1=list, list2=list):
	sortTest = [[list1[i], list2[i]] for i in range (len(list2))] # Joint les éléments dans de petites listes (pour qu'ils restent ensembles lors du trie)
	from operator import itemgetter                               # Importe "itemgetter", qui permet d'obtenir le trie selon 1 objet dans une liste (sortTest en a 2)
	sortTest      = sorted(sortTest, key=itemgetter(1)) # Trie selon la list2
	allSorted_ = [l[0] for l in sortTest]               # Re-Distribue les valeurs en 2 listes
	ySorted_   = [l[1] for l in sortTest]               # Re-Distribue les valeurs en 2 listes
	return allSorted_, ySorted_                         # Retourne ces listes

allListSorted, ySorted = sortList(allList, y)
###
print("Le genre le plus présent est", allListSorted[-1], "avec", ySorted[-1], "films/séries de ce genre")

### -> Graph :)       j'adore lire les documentations
plt.figure(figsize=(17, 8))                                                               # Taille de la fenêtre qui contient les 2 graphs
plt.subplot(1, 2, 1)                                                                      # Graph n°1
plt.subplots_adjust(left=0.04, bottom=0.35, right=1, top=0.802, wspace=-0.24, hspace=0.2) # Adjuste les valeurs de placement du graph
plt.title("Nombres films par genre")                                                      # Titre
plt.ylabel("Nombre de films")                                                             # Titre axe des y
plt.xlabel("Genres")                                                                      # Titre axe des x
plt.xticks(rotation=90)                                                                   # Valeur graduée à la vertical
plt.plot(allListSorted, ySorted)                                                          # Ajoute les valeurs
plt.grid()                                                                                # Ajoute la grille
for i in range(16): # Enlève les éléments mineurs pour un graph plus clair
    ySorted.pop(0)
    allListSorted.pop(0)
plt.subplot(1, 3, 3)                                      # Graph n°2
plt.pie(ySorted, labels=allListSorted, rotatelabels=True) # Graphique camembert :)
plt.show()                                                # Affiche le tout
plt.close()                                               # Ferme Matplotlib
##############################################################################





##########################  CONVERSION DES DATES  ############################

for l in tableau :                                                  # Pour tout les éléments du tableau ...
    if (l["date_added"] != "" and l["date_added"] != "00/00/0000"): # Regarde si la date est "valide"
        y = int(l["date_added"][6:10])                              # Récupère l'année
        m = int(l["date_added"][3:5])                               # Récupère le mois
        d = int(l["date_added"][0:2])                               # Récupère le jour
        l["date_added"] = [y , m , d]                               # Crée une liste contenant l'année, mois et jour
    else : l["date_added"] = [2021, 12, 31]                         # Si la date n'est pas "valide" alors remplace la date par le 31 décembre 2021

##############################################################################




###################  DATE PLUS JEUNE ET VIEUX FILM SUR NETFLIX  ###############
# Variables des records (et k = l'index de ce qui est mauvais)
sortiePremier = 3000
sortieDernier = 0
k             = 0

for l in tableau :                                    # Pour chaque éléments du tableau
    if (l["release_year"] != ""):                     # Si l'année de sortie est valide :
        if (int(l["release_year"]) > sortieDernier):  	# Si l'année analysée est au dessus du record
            sortieDernier = int(l["release_year"])    	# Actualise le record
        if (int(l["release_year"]) < sortiePremier):  	# Si l'année analysée est en dessous du record
            sortiePremier = int(l["release_year"])    	# Actualise le record
    else :              # Si la l'année n'est pas valide :
        tableau.pop(k)  # Enlève l'élément
        k-=1            # Enlève 1 à k car on a supprimé un élément
    k+=1                #Ajoute 1 à k pour changer l'index

# Affiche les résultats
print("Plus 'jeune' film sur Netflix est sortie en", sortieDernier)
print("Plus vieux film sur Netflix est sortie en",   sortiePremier)
###############################################################################




###########################  HORNY  ###########################################
horny = 0                           # Crée une variable
for l in tableau :                  # Pour chaque éléments du tableau ...
    if ("sex" in l["description"]): # Si le mot "sex" est contenue dans la description ...
            horny+=1                # ... Ajoute +1 à la variable 'libidineuse'
print("Eh beh ! il y a", horny, "films libidineux") # Affiche le résultat
##############################################################################




#######################  GRAPH FILMS AJOUTÉS CHAQUE ANNÉES ###################
year = [l["date_added"][0] for l in tableau]  # Crée une liste de toutes les dates d'ajout à Netflix
x = list(set(year))                           # Crée une liste des années sans doublons
x.sort()                                      # Range cette liste
y = [0 for i in x]                            # Crée une liste remplie de 0 et de longueur identque à la liste x
for l in year :                               # Pour chaque éléments du tableau de toutes les années
    y[x.index(l)] += 1                        # Ajoute 1 au nombre de films ajoutés cette année sur Netflix
for i in range(len(x)):                       # Convertit les années de nombre entier à chaîne de caractère pour un meilleur graph
    x[i] = str(x[i])

plt.figure(figsize=(9,6)) # Crée le graph et change sa taille
simplePlot(x, y, "Nombre de films ajoutés à Netflix chaque années", "Nombre de films", "Années", 90, True)
##############################################################################




############################  Date de sortie  ################################
year = [l["release_year"] for l in tableau] # Crée une liste de toutes les dates de sortie
x = list(set(year))                         # Crée une liste des années sans doublons
x.sort()                                    # Range cette liste
y = [0 for i in x]                          # Crée une liste remplie de 0 et de longueur identique à la liste x
for l in year :                             # Pour chaque éléments du tableau de toutes les années
    y[x.index(l)] += 1                      # Ajoute 1 au nombre de films sortie cette année
for i in range(len(x)):                     # Convertit les années de nombre entier à chaîne de caractère pour un meilleur graph
    x[i] = str(x[i])

plt.figure(figsize=(14,6)) # Crée le graph et change sa taille
simplePlot(x, y, "Nombre de films selon leur date de sortie", "Nombre de films", "Années", 90, True)
##############################################################################




#############################  LONGEST TITLE  ################################
record = 0                            # Crée une variable pour le record
titleL = ""                           # Crée une variable pour le nom du record
for l in tableau :                    # Pour chaque éléments du tableau
    if (len(l["title"]) > record):    # Si la longueur du titre est plus longue que celle du record
        record = len(l["title"])      # Actualise le record
        titleL = l["title"]           # Actualise le nom du record
print("Le plus long titre de film/série sur Netflix est '", titleL, "' avec", record, "charactères") # Affiche le record
##############################################################################




#################################  Âge  ######################################
rating = [l["rating"] for l in tableau]     # Crée une liste avec toutes les restrictions d'âges
allRating = list(set(rating))               # Crée une liste de ces restrictions sans doublons
y = [0 for i in range(len(allRating))]      # Crée une liste remplie de 0 et de longueur identique à la liste allRating
for l in tableau :                          # Pour chaque éléments du tableau :
    y[allRating.index(l["rating"])] += 1    # Ajoute 1 à la catégorie correspondante

allRating[allRating.index("")] = "vide"           # Remplace la catégorie vide par le nom "vide"
allRatingSorted, ySorted = sortList(allRating, y) # Range ces listes dans l'ordre croissant du nombre de films
simplePlot(allRatingSorted, ySorted, "Nombres de films par categories d'âges", "Nombre de films", "Categorie d'âge", 90, True) # Graph
##############################################################################




##########################  Âge && Netflix != chill  #############################
rating = [l["rating"] for l in tableau]   # Crée une liste avec toutes les restrictions d'âges
allRating = list(set(rating))             # Crée une liste de ces restrictions sans doublons
for i in ["UR", "", "NR"] :               # Enlève les catégorie non-définit
    allRating.remove(i)

### Liste toutes les catégories d'âges
print("voici la liste des catégorie retenues :")
for i in allRating :
    print("  - ", i)

### 'Tableau' fait-main pour les explications sur les catégories d'âges
print("Table des âges :                                                                                          \n",
	"TV-MA : 2027   =17  réservé aux adultes et inapproprié pour la jeune audience de moins de 17 ans            \n",
	"PG : 184       ~~~  Parental Guidance Suggested                                                             \n",
	"G : 37         ok+  All ages admitted                                                                       \n",
	"TV-Y : 143     ok+  approprié aux enfants                                                                   \n",
	"TV-Y7-FV : 95  ~~~  approprié aux enfants MAIS avec violence fantasy (Mickey qui frappe Dingo apr exemple)  \n",
	"TV-PG : 700    ~~~  éléments que les parents peuvent considérer inappropriés pour les enfants               \n",
	"NC-17 : 2      >17  Adults Only – No one 17 and under admitted.                                             \n",
	"TV-14 : 1698   =14  les parents peuvent considérer inappropriés pour les enfants âgés de moins de 14 ans    \n",
	"R : 508        ~~~  Under 17 requires accompanying parent or adult guardian.                                \n",
	"TV-G : 149     ~~~  plupart des parents peuvent considérer ce programme comme approprié pour les enfants    \n",
	"TV-Y7 : 169    ok+  désigné pour les enfants âgés de 7 ans                                                  \n",
	"PG-13 : 286    ~13  Parents Strongly Cautioned – Some material may be inappropriate for children under 13.  \n")

x = [str(i) for i in range(7, 19)]   # Crée une liste des âges de 7 à 18 (compris) au format chaîne de caractères
x[-1] = x[-1]+"+"                    # ajoute "+" au 18 pour faire -> 18+
y = [0 for i in range(7,19)]         # Crée une liste de 0
for l in tableau :                                                              # Pour chaque éléments du tableau :
    e = l["rating"]                                                             # Variable e = la catégorie analysée
    if e in ["PG-13", "TV-Y7", "TV-Y", "G", "PG", "TV-Y7-FV","TV-PG", "TV-G"] : # Si e est dans ces catégories :
        for i in range(0, 12):                                                  	# Pour les âges de 7 à 18+ :
            y[i] += 1                                                           		# Ajoute 1 à leur nombre de films/séries visibles à leur âge
    if e in ["R","TV-14"] :                                                     # Si e est dans ces catégories :
        for i in range(7, 12):                                                  	# Pour les âges de 14 à 18+ :
            y[i] += 1                                                           		# Ajoute 1 à leur nombre de films/séries visibles à leur âge
    if e == "NC-17" :                                                           # Pour la catégorie Adulte :
        y[11] += 1                                                              	# Ajoute 1 au nombre de films/séries visibles par les 18+

simplePlot(x, y, "Nombres de films visibles par âges", "Nombre de films", "Âge", 0, True) # Graph

x = ["Appropriés aux enfants", "Adulte requis"]             # Titre pour axe X
y = [0, 0]                                                  # Crée une liste pour stocker les nombres de films par catégorie
for l in tableau :                                          # Pour chaque éléments du tableau :
    if l["rating"] in ["G", "TV-Y", "TV-Y7-FV", "TV-Y7"] :  # Si l'élément analysé est dans ces catégories :
        y[0] += 1                                           # Ajoute 1 au nombre de cette catégorie
    if l["rating"] in ["PG-13", "PG", "TV-PG", "TV-G"] :    # Si l'élément analysé est dans ces catégories :
        y[1] += 1                                           # Ajoute 1 au nombre de cette catégorie

plt.bar(range(2), y, zorder=5.0)           # Histogramme
plt.grid(zorder=0)                         # Grille
plt.xticks(range(2), x)                    # Nomme les éléments sur l'axe des abscisses
plt.title("Contenue et présence adulte")   # Titre
plt.show()                                 # Affiche l'histogramme
plt.close()                                # Ferme Matplotlib
print("Il faut faire attention à ce que les enfants regarde !") # Message de prévention
##################################################################################




##############################  Interactivité  ###################################
### Tableau neuf (sans la conversion des temps)
tableau_bis = []
with open("netflix.csv", "r", encoding="UTF-8") as fichier :
    cles = fichier.readline()[:-1].split(";")
    for ligne in fichier :
        valeurs = ligne[:-1].split(";")
        dico = dict()
        for cle, valeur in zip(cles, valeurs) :
            dico[cle] = valeur
        tableau_bis.append(dico)

#####  -  Application avec Tkinter
import tkinter as tk # Importe Tkinter 
# Original : programme Hello World de la documentation officiel de Python sur Tkinter et aussi un peu de la documentation TkDocs

""" D'abord. Très important. Prière.
OOP   makes   me   go   yes                                        (Louis ->  OOP : Object Oriented Programming)
Bodging is my way to sucess
"""

def tagChanger(tag, id): # Fonction qui prend un "tag" donné et l'applique au label donné
    id.config(text=tag)

class Application(tk.Frame):                         # Crée la fenetre de l'application
    def __init__(self, master=None):                 # Initialisation
        super().__init__(master)                     # Initialisation automatique
        self.master = master
        self.master.title("Explorateur de donnée")   # titre de la fenêtre
        self.pack()                                  # Package (anglicisme) de la fenêtre
        self.create_widgets()                        # Execution du contenue

    def searchExe(self):                          # Fonction de recherche :
        self.element = self.entrySearch.get()     # Récupère ce qu'il faut rechercher
        self.tag = self.labelTag.cget("text")     # Récupère le tag dans lequel fouiller depuis le text des tags (astucieux, non ?)
        self.found = []                           # Crée une liste vide pour les élements trouvés
        self.output = ""                          # Crée une chaîne de caractères vide pour le résultat

        for l in tableau_bis :                                                               # Pour toutes les lignes dans le tableau neuf (sans conversion de temps) ...
            if (self.element) in l[self.tag] :                                               # ... Regarde si l'élément est présent dans la partie du tag donné
                self.found.append([l["title"], l["type"], l["release_year"], l["duration"]]) # Ajoute une liste d'éléments du film / de la série trouvé(e)
        
        if len(self.found) == 0 :                                                                        # Si rien n'a été trouvé ...
            self.output = "Désoler, " + self.element + " n'apparait pas"                                        # ... Assigne un message d'erreur au résultat
        else :                                                                                           # sinon
            self.output = self.element + " appears in " + self.tag + " for :\n"                                 # Annonce le résultat
            for i in self.found :                                                                               # Pour chaque éléments trouvés ...
                self.output += "  -  " + i[0] + " a " + i[1] + " released in " + i[2] + " (" + i[3] + ")" +"\n" # Ajoute une présentation clair de la trouvaille au résultat
        
        self.labelResult.config(text=self.output) # Retourne dans une case de texte le résultat


    def create_widgets(self):
        self.labelInput  = tk.Label(root,  text="Entrez votre recherche et choisissez votre catégorie :", pady=20)       # Crée un "titre"
        self.entrySearch = tk.Entry(root,  width=20)                                                                     # Crée une boîte de texte
        self.executeBT   = tk.Button(root, text="CHERCHER", fg="green", command=self.searchExe, pady=7)                  # Crée un bouton pour executer la recherche
        self.typeBtTitle = tk.Button(root, text="Titre",       command=lambda: tagChanger("title",       self.labelTag)) # Crée un bouton pour le tag : Titre
        self.typeBtDirec = tk.Button(root, text="Réalisateur", command=lambda: tagChanger("director",    self.labelTag)) # Crée un bouton pour le tag : Réalisateur
        self.typeBtCast  = tk.Button(root, text="Acteur",      command=lambda: tagChanger("cast",        self.labelTag)) # Crée un bouton pour le tag : Acteur/Actrice
        self.typeBtTime  = tk.Button(root, text="Durée",       command=lambda: tagChanger("duration",    self.labelTag)) # Crée un bouton pour le tag : Durée
        self.typeBtDesc  = tk.Button(root, text="Description", command=lambda: tagChanger("description", self.labelTag)) # Crée un bouton pour le tag : Description

        self.labelResult = tk.Label(root, height=30)                     # Crée un text pour le résultat
        self.labelTagDes = tk.Label(root, text="Catégorie :", pady=20)   # Crée un text pour le annoncer les boutons des tags
        self.labelTag    = tk.Label(root, text="cast")                   # Crée un bouton pour montrer le tag actuellement choisi

        self.labelInput. pack(side="top") # Pack le texte (et donc l'affiche)
        self.entrySearch.pack(side="top") # Pack la boîte de texte
        self.executeBT.  pack(side="top") # Pack le bouton
        self.labelTagDes.pack(side="top") # Pack le texte
        self.labelTag.   pack(side="top") # Pack le texte
        self.typeBtTitle.pack(side="top") # Pack le bouton
        self.typeBtDirec.pack(side="top") # Pack le bouton
        self.typeBtCast. pack(side="top") # Pack le bouton
        self.typeBtTime. pack(side="top") # Pack le bouton
        self.typeBtDesc. pack(side="top") # Pack le bouton
        self.labelResult.pack(side="top") # Pack le texte

        self.quit = tk.Button(root, text="QUITTER", fg="red", command=self.master.destroy) # Crée un bouton Quitter
        self.quit.pack(side="bottom")                                                      # Pack le bouton Quitter


root = tk.Tk()
root.geometry("500x800")       # Taille de la fenêtre
app = Application(master=root) # Lance l'application
app.mainloop()                 # Repète en boucle l'application

##################################################################################




#######################  Actors (Grosse partie)  #############################
actors = [l["cast"].split(",") for l in tableau if (l["cast"] != "")]  # Liste de tout les castings
allActors = []                                                         # Crée une liste pour tout les acteurs
for l in actors :                                                      # Pour chaque casting :
	for i in l :                                                       # Pour chaque acteurs dans ce casting :
		i = i.strip()                                                  # Enlève l'espace avant chaque nom
		allActors.append(i)                                            # Ajoute cette acteur à la liste
listActors = list(set(allActors))                                      # Crée une liste des acteurs qui n'a aucun doublons
y = [0 for i in range(len(listActors))]                                # Crée une liste remplie de 0 de longueur identique à la listActors
for i in allActors :                                                   # Pour chaque apparition d'acteurs sur Netflix :
	y[listActors.index(i)] += 1                                        # Ajoute 1 au nombre de films joué par cette acteur             index() est super lent hélas :(

### -> Moyene
movieTotal = 0           # Total des films
for i in y :             # Pour chaque acteurs :
    movieTotal += i      # Ajoute le nombre de films/séries joués
print("In average, actors on Netflix act in", round(movieTotal/(len(listActors))), "movies/series") # Affiche le résultat tout en calculant la moyenne

maxMovie = 0          # Le plus grand nombre de films joué par une seule personne
for l in y :          # Pour chaque acteurs :
    if (l>maxMovie):  # Si il bat le record
        maxMovie=l    # Actualise le record

x_ = [i for i in range(maxMovie+1)] # Crée une liste numéroté de 0 à maxMovie
y_ = [i for i in range(maxMovie+1)] # Crée une liste numéroté de 0 à maxMovie
for i in y :                        # Pour tout les acteurs
    y_[i] += 1                      # Ajoute 1 au nombre de films/séries qu'ils ont joués
for i in range(len(x_)) :           # Convertit toute la liste x en chaîne de caractères pour un meilleur graph
    x_[i] = str(x_[i])

x_.pop(0) # Enlève l'élément 0 car aucun acteur n'a joué dans 0 films (logique)
y_.pop(0)

simplePlot(x_, y_, "Nombres du total de films joués par un/une acteur/actrice", "Nombre d'acteurs/actrices", "Total de films", 90, True) # Graph

for i in range(len(y)-1, -1, -1) :  # Pour tout les acteurs du dernier de la liste au premier
    if (y[i] <= 13) :               # Si l'acteur a moins de 14 films :
        y.pop(i)                    # Supprime l'acteur des données
        allActors.pop(i)

allActorsSorted, ySorted = sortList(listActors, y)                                                  # Range les valeurs
print("L'acteur qui apparait le plus est", allActorsSorted[-1], "avec", ySorted[-1], "apparitions") # Affiche des résultats divers

### -> Graph Double
plt.figure(figsize=(16, 8))                                                                  # Taille de la fenêtre qui contient les 2 graphs
plt.subplot(1, 2, 1)                                                                         # Graph n°1
plt.subplots_adjust(left=0.04, bottom=0.35, right=1, top=0.802, wspace=-0.24, hspace=0.2)    # Adjuste les valeurs de placement du graph
plt.title("Nombres films joués par acteur/actrice")                                          # Titre
plt.ylabel("Nombre de films")                                                                # Titre axe des y
plt.xlabel("Acteurs")                                                                        # Titre axe des x
plt.xticks(rotation=90)                                                                      # Valeur graduée à la vertical
plt.plot(allActorsSorted, ySorted) # Ajoute les valeurs
plt.grid()                                                                                   # Ajoute la grille
plt.subplot(1, 3, 3)                                                                         # Graph n°2
plt.pie(ySorted, labels=allActorsSorted, rotatelabels=True)                                  # Graphique camembert :)
plt.show()                                                                                   # Affiche le tout
plt.close()                                                                                  # Ferme Matplotlib
##############################################################################




##################  Well-known people (Actors II)  ###########################
### -> Barack Obama & George Clooney
def actorFinder(name) :
    print(name, "appears in :")
    found = False
    for l in tableau :
        if (name in l["cast"]):
            print("  - ", l["title"], "a", l["type"], "released in", l["release_year"])
            found = True
    if (found == False) :
        print("Désoler, cette personne n'est pas sur Netflix")
actorFinder("Barack Obama")
actorFinder("George Clooney")
print("Conclusion : GEORGE CLOONEY IS INSIDE !!!!!")

##### Interactivity !     version antiquité
actorFinder(input("Donnez moi un nom d'acteur/actrice ou d'une personne connue  :  ")) #    :)

answer = input("Encore ? Y/N")
while(answer == "Y") :
    actorFinder(input("Donnez moi un nom d'acteur/actrice ou d'une personne connue  :  "))
    answer = input("Encore ? Y/N")

##### Version compliqué :)
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Chercheur d'acteurs !")
        self.pack()
        self.create_widgets()

    def searchExe(self):
        self.element = self.entrySearch.get()
        self.found = []
        self.output = ""
        for l in tableau : # Search
            if (self.element) in l["cast"] :
                self.found.append([l["title"], l["type"], l["release_year"]])
        if len(self.found) == 0 : # Nothing ?
            self.output = "Désoler, " + self.element + " n'apparait pas"
        else :
            self.output = self.element + " appears in :\n"
            for i in self.found :
                self.output += "  -  " + i[0] + " a " + i[1] + " released in " + i[2] + "\n"
        self.labelResult.config(text=self.output)

    def create_widgets(self):
        self.labelInput  = tk.Label(   root, text="Entrez le nom et/ou prénom d'un acteur ou d'une actrice :", pady=20)
        self.executeBT   = tk.Button(  root, text="CHERCHER", fg="green", command=self.searchExe, pady=7)
        self.labelResult = tk.Label(   root, height=20)
        self.entrySearch = tk.Entry(   root, width=20)

        self.labelInput.  pack(side="top")
        self.entrySearch. pack(side="top")
        self.executeBT.   pack(side="top")
        self.labelResult. pack(side="top")

        self.quit = tk.Button(root, text="QUITTER", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")


root = tk.Tk()
root.geometry("500x500")
app = Application(master=root)
app.mainloop()

##################################################################################

print("Merci beaucoup d'avoir lu jusqu'au bout !")