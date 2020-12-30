# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt # Importation de Matplotlib <3

######################  Importation du tableau  ##############################
tableau = []
with open("netflix.csv", "r", encoding="UTF-8") as fichier :
    cles = fichier.readline()[:-1].split(";")
    for ligne in fichier :
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

# Code plus optimisé mais pas "adaptatif" :
x = ["TV Show", "Movie"]
y = [0, 0]
for i in tableau:
    if (i["type"] == "TV Show"):
        y[0] += 1
    else :
        y[1] += 1

plt.bar(range(2), y, zorder=5.0)
plt.grid(zorder=0)
plt.xticks(range(2), ["Show télévisé", "Film"])
plt.title("Type de programme")
plt.show()
plt.close()

##############################################################################




###########################  Tableau des temps  #############################
time = []
k = 0
id_remove = 0
for l in tableau  :
    if (l["type"] == "Movie"):
        n = l["duration"]
        n = n[0:len(n)-4]
        if (n != ""):
            time.append(int(n))
        else:
            id_remove = k
    k+=1
#print(tableau[id_remove]) # The Memphis Belle: A Story of a ...
tableau.pop(id_remove)
# tout ça pour un tableau Time qui ne sert pas à grand chose ...

######## Total de films
i=0
for l in tableau:
    if (l["type"]=="Movie"):
        i+=1
print("There are :", i, "movies on Netflix")
###############################################################################




#########################  CONVERTION DUREE  ##################################
for l in tableau :
    if (l["type"] == "Movie"):
        l["duration"] = int(l["duration"][0:len(l["duration"])-4])
###############################################################################




#########################   DUREE  ############################################
maxi = 0
id_maxi = ""
mini = 300
id_mini = ""
for l in tableau:
    if (l["type"] == "Movie"):
        if (l["duration"] > maxi):
            maxi = l["duration"]
            id_maxi = l
        if (l["duration"] < mini):
            mini = l["duration"]
            id_mini = l
print("Shortest movie : ", id_mini["title"], "with only ", mini, " minutes")
print("Longest movie : ", id_maxi["title"], " with ", maxi, " minutes")
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
x = list(set(time))
y = [0 for i in x]
for l in time :
    y[x.index(l)] += 1 # CLEAN ! ça c'est beau ! C'est ça qu'on veut ! xD
plt.plot(x, y)
plt.title("Nombre de films par durée")
plt.ylabel("Nombre de films")
plt.xlabel("Durées")
plt.show()
plt.close()
###############################################################################




######################### Temps : Max et Min Date  ############################
yearMax = 0
monthMax= 0
dayMax  = 0

yearMin = 3000
monthMin= 3000
dayMin  = 3000

# 2 2 / 0 9 / 2 0 1 7
# 0 1 2 3 4 5 6 7 8 9

for l in tableau :
    if (l["date_added"] != "" and l["date_added"] != "00/00/0000"):
        #print(l["date_added"][6:10], l["date_added"][3:5], l["date_added"][0:2])          DEBUG
        y = int(l["date_added"][6:10])
        m = int(l["date_added"][3:5])
        d = int(l["date_added"][0:2])

        recordMax = False
        if (y > yearMax) : recordMax = True
        if (m > monthMax and y >= yearMax) : recordMax = True
        if (d > dayMax and m >= monthMax and y > yearMax) : recordMax = True

        if (recordMax == True) :
            yearMax = y
            monthMax= m
            dayMax  = d

        recordMin = False
        if (y < yearMin) : recordMin = True
        if (m < monthMin and y <= yearMin) : recordMin = True
        if (d < dayMin and m <= monthMin and y < yearMin) : recordMin = True

        if (recordMin == True) :
            yearMin = y
            monthMin= m
            dayMin  = d
            #print(y, m, d)   #c'est jolie à regarder

print("Latest movie/series added : ", yearMax, monthMax, dayMax)
print("First movie/series added : " , yearMin, monthMin, dayMin)
###############################################################################




###################################  Genres  ##################################
listType = [l["listed_in"].split(",") for l in tableau if (l["listed_in"] != "")]
allList = []
y = []
for l in listType :
    for i in l :
        i = i.strip() # Striped because there is a space at the beginning of some of them
        if (i in allList) : # the "in" makes everything slower and I don't know how to solve it otherwise
            y[allList.index(i)] += 1
        else:
            allList.append(i)
            y.append(1) # not 0 because it has to be found to be added to the list
print("There are",len(allList),"different show categories")

### -> Sorting part
sortTest = [[allList[i], y[i]] for i in range (len(y))]
from operator import itemgetter
sortTest      = sorted(sortTest, key=itemgetter(1))
allListSorted = [l[0] for l in sortTest]
ySorted       = [l[1] for l in sortTest]
###
print("The most appeared actor is", sortTest[-1][0], "with", sortTest[-1][1], "apperances")

### -> Graph :)       j'adore lire les documentations quand elles sont bien faites
plt.figure(figsize=(17, 8))
plt.subplot(1, 2, 1)
plt.subplots_adjust(left=0.04, bottom=0.35, right=1, top=0.802, wspace=-0.24, hspace=0.2)
plt.title("Nombres films par genre")
plt.ylabel("Nombre de films")
plt.xlabel("Genres")
plt.xticks(rotation=90)
plt.plot(allListSorted, ySorted)
plt.grid()
for i in range(16):
    ySorted.pop(0)
    allListSorted.pop(0)
plt.subplot(1, 3, 3)
plt.pie(ySorted, labels=allListSorted, rotatelabels=True)
plt.show()
plt.close()
##############################################################################





###################  CONVERSION DES DATES CAR JE M'ENNUIE  ###################

for l in tableau :
    if (l["date_added"] != "" and l["date_added"] != "00/00/0000"):
        y = int(l["date_added"][6:10])
        m = int(l["date_added"][3:5])
        d = int(l["date_added"][0:2])
        l["date_added"] = [y , m , d]
    else : l["date_added"] = [2021, 12, 31]

for i in range (len(tableau)) :
    if (type(tableau[i]["date_added"][0]) == "str"):
        print("OOOOOF")
##############################################################################




###################  DATE PLUS JEUNE ET VIEUX FILM SUR NETFLIX  ###############
sortiePremier = 3000
sortieDernier = 0
k             = 0

for l in tableau :
    #print(l["release_year"])        DEBUG
    if (l["release_year"] != ""):
        if (int(l["release_year"]) > sortieDernier):
            sortieDernier = int(l["release_year"])
        if (int(l["release_year"]) < sortiePremier):
            sortiePremier = int(l["release_year"])
    else :
        tableau.pop(k)
        k-=1
    k+=1

print("Youngest movie/series on Netflix : ", sortieDernier)
print("Oldest movie/series on Netflix : "  , sortiePremier)
###############################################################################




###########################  HORNY  ###########################################
horny = 0
for l in tableau :
    if ("sex" in l["description"]):
            horny+=1
print("Ew... There are :", horny, "horny movies/series")
##############################################################################




#######################  GRAPH FILMS AJOUTÉS CHAQUE ANNÉES ###################
year = [l["date_added"][0] for l in tableau]
x = list(set(year))
x.sort()
y = [0 for i in x]
for l in year :
    y[x.index(l)] += 1 # CLEAN ! ça c'est beau ! C'est ça qu'on veut ! xD
for i in range(len(x)):
    x[i] = str(x[i])
plt.figure(figsize=(9,6))
plt.title("Nombre de films ajoutés à Netflix chaque années")
plt.ylabel("Nombre de films")
plt.xlabel("Années")
plt.xticks(rotation=90)
plt.plot(x, y)
plt.grid()
plt.show()
plt.close()
##############################################################################




#############################  LONGEST TITLE  ################################
record = 0
for l in tableau :
    if (len(l["title"]) > record):
        record = len(l["title"])
print("Longest title :", record)
##############################################################################




###########################  Âge  ############################################
rating = [l["rating"] for l in tableau]
allRating = list(set(rating))
y = [0 for i in range(len(allRating))]
for l in tableau :
    j=0
    for i in allRating :
        if (l["rating"] == i) :
            y[j] += 1
        j+=1
'''for i in range(len(allRating)) :           # Debug fun
    print(allRating[i], ":", y[i])'''
allRating[allRating.index("")] = "vide"
plt.title("Nombres de films par categories d'âges")
plt.ylabel("Nombre de films")
plt.xlabel("Categorie d'âge")
plt.xticks(rotation=90)
plt.plot(allRating, y)
plt.grid()
plt.show()
plt.close()
##############################################################################




##########################  Âge && Netflix != chill  #############################
rating = [l["rating"] for l in tableau]
allRating = list(set(rating))
for i in ["UR", "", "NR"] :
    allRating.remove(i)

print("voici la liste des catégorie retenues :")
for i in allRating :
    print("  - ", i)

# Mon dieu tuez moi           never again
print("Table des âges :\nTV-MA : 2027   =17  réservé aux adultes et inapproprié pour la jeune audience de moins de 17 ans\nPG : 184       ~~~  Parental Guidance Suggested\nG : 37         ok+  All ages admitted\nTV-Y : 143     ok+  approprié aux enfants\nTV-Y7-FV : 95  ~~~  approprié aux enfants MAIS avec violence fantasy (Mickey qui frappe Dingo apr exemple)\nTV-PG : 700    ~~~  éléments que les parents peuvent considérer inappropriés pour les enfants\nNC-17 : 2      >17  Adults Only – No one 17 and under admitted.\nTV-14 : 1698   =14  les parents peuvent considérer inappropriés pour les enfants âgés de moins de 14 ans\nR : 508        ~~~  Under 17 requires accompanying parent or adult guardian.\nTV-G : 149     ~~~  plupart des parents peuvent considérer ce programme comme approprié pour les enfants\nTV-Y7 : 169    ok+  désigné pour les enfants âgés de 7 ans\nPG-13 : 286    ~13  Parents Strongly Cautioned – Some material may be inappropriate for children under 13.")

x = [str(i) for i in range(7, 19)]
x[-1] = x[-1]+"+"
y = [0 for i in range(7,19)]
for l in tableau :
    e = l["rating"]
    if e in ["PG-13", "TV-Y7", "TV-Y", "G", "PG", "TV-Y7-FV","TV-PG", "TV-G"] :
        for i in range(0, 12):
            y[i] += 1
    if e in ["R","TV-14"] :
        for i in range(7, 12):
            y[i] += 1
    if e == "NC-17" :
        y[11] += 1

plt.title("Nombres de films visibles par âges")
plt.ylabel("Nombre de films")
plt.xlabel("âge")
plt.plot(x, y)
plt.grid()
plt.show()
plt.close()


x = ["Appropriés aux enfants", "Adulte requis"]
y = [0, 0]
for l in tableau :
    if l["rating"] in ["G", "TV-Y", "TV-Y7-FV", "TV-Y7"] :
        y[0] += 1
    if l["rating"] in ["PG-13", "PG", "TV-PG", "TV-G"] :
        y[1] += 1

plt.bar(range(2), y, zorder=5.0)
plt.grid(zorder=0)
plt.xticks(range(2), x)
plt.title("Contenue et présence adulte")
plt.show()
plt.close()
print("Il faut faire attention à ce que les enfants regarde !")
##################################################################################




##############################  Interactivité  ###################################

tableau_bis = []
with open("netflix.csv", "r", encoding="UTF-8") as fichier :
    cles = fichier.readline()[:-1].split(";")
    for ligne in fichier :
        valeurs = ligne[:-1].split(";")
        dico = dict()
        for cle, valeur in zip(cles, valeurs) :
            dico[cle] = valeur
        tableau_bis.append(dico)

import tkinter as tk
# <3 fun is coming <3        Object Oriented Programming makes me go YES

def tagChanger(tag, id): # The art of Bodging :)
    id.config(text=tag)

class Application(tk.Frame): # Original : Hello World program from Python official documentation on Tkinter
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Explorateur de donnée")
        self.pack()
        self.create_widgets()

    def searchExe(self):
        self.element = self.entrySearch.get()
        self.tag = self.labelTag.cget("text")
        self.found = []
        self.output = ""
        for l in tableau_bis : # Search
            if (self.element) in l[self.tag] :
                self.found.append([l["title"], l["type"], l["release_year"], l["duration"]])
        if len(self.found) == 0 : # Nothing ?
            self.output = "Désoler, " + self.element + " n'apparait pas"
        else :
            self.output = self.element + " appears in " + self.tag + " for :\n"
            for i in self.found :
                self.output += "  -  " + i[0] + " a " + i[1] + " released in " + i[2] + " (" + i[3] + ")" +"\n"
        self.labelResult.config(text=self.output)


    def create_widgets(self):
        self.labelInput  = tk.Label(root,  text="Entrez votre recherche et choisissez votre catégorie :", pady=20)
        self.entrySearch = tk.Entry(root,  width=20)
        self.executeBT   = tk.Button(root, text="CHERCHER", fg="green", command=self.searchExe, pady=7)
        self.typeBtTitle = tk.Button(root, text="Titre",       command=lambda: tagChanger("title",       self.labelTag))
        self.typeBtDirec = tk.Button(root, text="Réalisateur", command=lambda: tagChanger("director",    self.labelTag))
        self.typeBtCast  = tk.Button(root, text="Acteur",      command=lambda: tagChanger("cast",        self.labelTag))
        self.typeBtTime  = tk.Button(root, text="Durée",       command=lambda: tagChanger("duration",    self.labelTag))
        self.typeBtDesc  = tk.Button(root, text="Description", command=lambda: tagChanger("description", self.labelTag))

        self.labelResult = tk.Label(root, height=30)
        self.labelTagDes = tk.Label(root, text="Catégorie :", pady=20)
        self.labelTag    = tk.Label(root, text="cast")

        self.labelInput. pack(side="top")
        self.entrySearch.pack(side="top")
        self.executeBT.  pack(side="top")
        self.labelTagDes.pack(side="top")
        self.labelTag.   pack(side="top")
        self.typeBtTitle.pack(side="top")
        self.typeBtDirec.pack(side="top")
        self.typeBtCast. pack(side="top")
        self.typeBtTime. pack(side="top")
        self.typeBtDesc. pack(side="top")
        self.labelResult.pack(side="top")

        self.quit = tk.Button(root, text="QUITTER", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")


root = tk.Tk()
root.geometry("500x800")
app = Application(master=root)
app.mainloop()

##################################################################################




#######################  Actors (Grosse partie)  #############################
actors = [l["cast"].split(",") for l in tableau if (l["cast"] != "")]
allActors = []
y = []

### -> Fun Debug Stats
#nb = 0
#action = 0
#dupliquat = 0
###

for l in actors :
    for i in l :
        i = i.strip() # Striped because there is a space at the beginning of some of them
        #nb+=1
        if (i in allActors) : # the "in" makes everything slower and I don't know how to solve it otherwise
            y[allActors.index(i)] += 1
            #action+=1
            #dupliquat+=1
        else:
            allActors.append(i)
            y.append(1) # not 0 because it has to be found to be added to the list
            #action +=1
print("There are",len(allActors),"different actors")

### -> Fun Debug Stats
#print("Fun debug stats : There were ",nb,"actors to check with", dupliquat, "duplicates checked...      nice code (smirk face)")
###

### -> Average
allMovie = 0
for i in y :
    allMovie += i
print("In average, actors on Netflix act in", round(allMovie/(len(allActors)-1)), "movies/series")

maxMovie = 0
for l in y :
    if (l>maxMovie):
        maxMovie=l
y_ = [i for i in range(maxMovie+1)]
y_.sort() # useless but who knows
x_ = [i for i in range(y_[-1]+1)]
for i in y :
    x_[i] += 1
for i in range(len(y_)) :
    y_[i] = str(y_[i])

x_.pop(0) # Remove the 0 because how could actors act 0 movies
y_.pop(0)

plt.title("Nombres du total de films joués par un/une acteur/actrice")
plt.ylabel("Nombre d'acteurs/actrices")
plt.xlabel("Total de films")
plt.xticks(rotation=90)
plt.plot(y_, x_)
plt.grid()
plt.show()
plt.close()
###

for i in range(len(y)-1, -1, -1) :
    if (y[i] <= 13) : # 13 is already enough
        y.pop(i)
        allActors.pop(i)
"""for i in range(len(allActors)) :       # Debug fun
    print(allActors[i], ":", y[i])"""

### -> Sorting part
sortTest = [[allActors[i], y[i]] for i in range (len(y))]
from operator import itemgetter
sortTest = sorted(sortTest, key=itemgetter(1))
allActorsSorted = [l[0] for l in sortTest]
ySorted         = [l[1] for l in sortTest]
###
print("The most appeared actor is", sortTest[-1][0], "with", sortTest[-1][1], "apperances") # Already calculated with maxMovie but this line was coded before :)

### -> Graph :)       j'adore lire les documentations quand elles sont bien faites
plt.figure(figsize=(16, 8))
plt.subplot(1, 2, 1)
plt.subplots_adjust(left=0.04, bottom=0.35, right=1, top=0.802, wspace=-0.24, hspace=0.2)
plt.title("Nombres films joués par acteur/actrice")
plt.ylabel("Nombre de films")
plt.xlabel("Acteurs")
plt.xticks(rotation=90)
plt.plot(allActorsSorted, ySorted)
plt.grid()
plt.subplot(1, 3, 3)
plt.pie(ySorted, labels=allActorsSorted, rotatelabels=True)
plt.show()
plt.close()
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

### Interactivity !
actorFinder(input("Donnez moi un nom d'acteur/actrice ou d'une personne connue  :  ")) #    :)

answer = input("Encore ? Y/N")
while(answer == "Y") :
    actorFinder(input("Donnez moi un nom d'acteur/actrice ou d'une personne connue  :  "))
    answer = input("Encore ? Y/N")

##### Version compliqué :)
import tkinter as tk

class Application(tk.Frame): # Original : Hello World program from Python official documentation on Tkinter
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
        self.labelInput  = tk.Label(root, text="Entrez le nom et/ou prénom d'un acteur ou d'une actrice :", pady=20)
        self.entrySearch = tk.Entry(root, width=20)
        self.executeBT   = tk.Button(root, text="CHERCHER", fg="green", command=self.searchExe, pady=7)
        self.labelResult = tk.Label(root, height=20)

        self.labelInput.pack(side="top")
        self.entrySearch.pack(side="top")
        self.executeBT.pack(side="top")
        self.labelResult.pack(side="top")

        self.quit = tk.Button(root, text="QUITTER", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")


root = tk.Tk()
root.geometry("500x500")
app = Application(master=root)
app.mainloop()

##################################################################################

print("Merci beaucoup d'avoir lu jusqu'au bout !")