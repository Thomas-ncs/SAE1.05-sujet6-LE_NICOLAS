from fichier import * #ont import le fichier nous permettant d'accéder aux donner
from tkinter import *
import matplotlib.pyplot as plt
import numpy as np



date_2010 = []
dico_A = {}
dico_N = {}
ba = []
arbent = []
date_2024 = []
a =0
region_2010 =[]
region_2024 =[]
for i in range(len(date)):

    if int(date[i]) < 202400 and int(date[i]) > 201000:
        date_2010.append([nom[i],date[i],post[i],rr[i],lat[i],long[i]])
    if int(date[i]) > 202400:
        date_2024.append([nom[i],date[i],post[i],rr[i],lat[i],long[i]])


dico_2024 = {}
dico_2010 = {}
for item in date_2010:  
    key = item[0]  
    value = item[1:]  
    if key in dico_2010:
        dico_2010[key].append(value)  
    else:
        dico_2010[key] = [value] 

for objet in date_2024:
    clef = objet[0]
    valeur = objet[1:]
    if clef in dico_2024:
        dico_2024[clef].append(valeur)
    else:
        dico_2024[clef] = [valeur]





clés_a_supprimer= [i for i in dico_2024 if len(dico_2024[i]) != 13]
for clé in clés_a_supprimer:
    del dico_2024[clé]



clés_a_supprimer = [i for i in dico_2010 if len(dico_2010[i]) != 14 * 12]
for clé in clés_a_supprimer:
    del dico_2010[clé]

comparaison_2010 = dict(dico_2010) #copié une variable comparaison pour toujour avoir la variable dico_2010



a = 0
for i in comparaison_2010.keys():
    for u in range(len(comparaison_2010[i])):
        a = comparaison_2010[i][u][2] + a
    comparaison_2010[i] = a
    a=0
plus_grand = []
for i in comparaison_2010.items():
    plus_grand.append([i[0],i[1]])

plus_grand.sort(key=lambda x: x[1], reverse=True)

# Afficher la liste triée

del plus_grand[51:]

cles_plus_grand = {clé for clé, _ in plus_grand}

# Supprimer les clés qui ne sont pas dans cles_plus_grand en créant un dictionnaire
for clé in list(dico_2010.keys()):  # On parcourt une copie des clés pour éviter des erreurs pendant la suppression
    if clé not in cles_plus_grand:
        del dico_2010[clé]


list_2010=[]
list_2024= []



fenetre = Tk()  #affiche graphiquement les nom du dictionnaire 

fenetre.geometry("275x100")

listbox = Listbox(fenetre)
scrollbar = Scrollbar(fenetre)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
for item in dico_2010.keys():
    listbox.insert(END, item)

listbox.insert(END, i)
listbox.pack(side=LEFT, fill=BOTH, expand=True)
scrollbar.pack(side=RIGHT, fill=Y)


fenetre.mainloop() #sort de l'afficheur puis tape le nom du département

nom = str(input('un nom: en majuscule'))
def graphique_2010(nom):
    a = []
    b = []
    if nom in dico_2010.keys():
        for i in dico_2010.keys():
            for u in range(len(dico_2010[i])):
                a.append([2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024])
                b.append(dico_2010[i][u][3])
    plt.plot(a,b)
    plt.ylabel('précipitation en milimètre')
    plt.ylabel('en année')
    plt.show()
a = graphique_2010(nom)
print(a)

    




