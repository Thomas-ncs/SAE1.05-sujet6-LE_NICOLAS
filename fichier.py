import os
import csv


lat = []
long = []
post = []
rr = []
date = []
nom = []
date_post = []
all_data = []

for subdir, _, files in os.walk(r"C:\Users\le_mi\OneDrive\Bureau\dossier_projet"): #parcourir le dossier principale
    for file in files:
        if file.endswith(".csv"): #
            with open(os.path.join(subdir, file), 'r') as csvfile: #ouvrir les fichier csv dans les sous dossier
                line =csv.reader(csvfile,delimiter=';')
                next(line) #a chaque ouverture de dossier ont ignore la première liste
                for u in line:
                    val = u[6]  # les espaces
                    if val == "": #remplacer les données vide par des 0
                        rr.append(0)
                    else:
                        flotant = float(val) #convertir les chiffres str par des float
                        rr.append(flotant) 
                    post.append(u[0]) #numéro de post de la station
                    date.append(int(u[5])) #date des prélèvement
                    nom.append(u[1]) #nom de la commune
                    long.append(u[3]) #longitude
                    lat.append(u[2]) #latitude
