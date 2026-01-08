import tkinter as tk
from tkinter import filedialog

file = None
choix = None

def sauvegarder_choix(selection):
    global choix
    choix = selection

def choisir_fichier():
    # Ouvre une boîte de dialogue pour sélectionner un fichier
    chemin_fichier = filedialog.askopenfilename(title="Sélectionner un fichier")
    
    # Affiche le chemin du fichier sélectionné
    if chemin_fichier:
        label_chemin.config(text=f"Fichier sélectionné : {chemin_fichier}")
        global file
        file = chemin_fichier
    else:
        label_chemin.config(text="Aucun fichier sélectionné")


def csvfileLinux(file_path):
    f = open(file_path, 'r', encoding='utf-8')
    
    lignes = f.readlines()
    
    # a: liste des éléments avant le ":"
    a = []
    # b: liste des éléments après le ":"
    b = []
    
    for ligne in lignes:
        ligne = ligne.strip()
        if ':' in ligne:
            elements = ligne.split(':', 1)
            a.append(elements[0])
            b.append(elements[1] if len(elements) > 1 else "")
    
    # Trouver toutes les positions de BEGIN:VEVENT
    positions_begin = []
    for index, element in enumerate(a):
        if element == 'BEGIN' and b[index] == 'VEVENT':
            positions_begin.append(index)
    
    # Extraire les événements
    evenements = []
    for i in range(len(positions_begin)):
        if i < len(positions_begin) - 1:
            debut = positions_begin[i]
            fin = positions_begin[i + 1]
        else:
            debut = positions_begin[i]
            # Trouver le END:VEVENT correspondant
            fin = debut
            for j in range(debut, len(a)):
                if a[j] == 'END' and b[j] == 'VEVENT':
                    fin = j + 1
                    break
        
        # Créer un dictionnaire pour cet événement
        evenement = {}
        for k in range(debut, fin):
            cle = a[k]
            valeur = b[k]
            # Ignorer BEGIN et END
            if cle not in ['BEGIN', 'END']:
                evenement[cle] = valeur
        evenements.append(evenement)
    
    # Collecter toutes les colonnes uniques
    colonnes = []
    for evenement in evenements:
        for cle in evenement.keys():
            if cle not in colonnes:
                colonnes.append(cle)
    
    f.close()

    # Écrire le fichier CSV
    f2 = open('SortieCSV_Linux.csv', 'w', encoding='utf-8')
    
    # Écrire l'en-tête
    ligneEntete = ";".join(colonnes) + "\n"
    f2.write(ligneEntete)
    
    # Écrire les données
    for evenement in evenements:
        ligne_data = []
        for colonne in colonnes:
            valeur = evenement.get(colonne, "")  # Valeur vide si la colonne n'existe pas
            ligne_data.append(valeur)
        ligne = ",".join(ligne_data) + "\n"
        f2.write(ligne)
    # Écrire le fichier CSV
    f2 = open('SortieCSV_Linux.csv', 'w', encoding='utf-8')
    
    # Écrire l'en-tête
    ligneEntete = ",".join(colonnes) + "\n"
    f2.write(ligneEntete)
    
    # Écrire les données
    for evenement in evenements:
        ligne_data = []
        for colonne in colonnes:
            valeur = evenement.get(colonne, "")  # Valeur vide si la colonne n'existe pas
            ligne_data.append(valeur)
        ligne = ",".join(ligne_data) + "\n"
        f2.write(ligne)
    
    f2.close()
    
    print(f"Fichier CSV créé avec {len(evenements)} événements et {len(colonnes)} colonnes")
def csvfileWin(file_path):
    f = open(file_path, 'r', encoding='utf-8')
    
    lignes = f.readlines()
    
    # a: liste des éléments avant le ":"
    a = []
    # b: liste des éléments après le ":"
    b = []
    
    for ligne in lignes:
        ligne = ligne.strip()
        if ':' in ligne:
            elements = ligne.split(':', 1)
            a.append(elements[0])
            b.append(elements[1] if len(elements) > 1 else "")
    
    # Trouver toutes les positions de BEGIN:VEVENT
    positions_begin = []
    for index, element in enumerate(a):
        if element == 'BEGIN' and b[index] == 'VEVENT':
            positions_begin.append(index)
    
    # Extraire les événements
    evenements = []
    for i in range(len(positions_begin)):
        if i < len(positions_begin) - 1:
            debut = positions_begin[i]
            fin = positions_begin[i + 1]
        else:
            debut = positions_begin[i]
            # Trouver le END:VEVENT correspondant
            fin = debut
            for j in range(debut, len(a)):
                if a[j] == 'END' and b[j] == 'VEVENT':
                    fin = j + 1
                    break
        
        # Créer un dictionnaire pour cet événement
        evenement = {}
        for k in range(debut, fin):
            cle = a[k]
            valeur = b[k]
            # Ignorer BEGIN et END
            if cle not in ['BEGIN', 'END']:
                evenement[cle] = valeur
        evenements.append(evenement)
    
    # Collecter toutes les colonnes uniques
    colonnes = []
    for evenement in evenements:
        for cle in evenement.keys():
            if cle not in colonnes:
                colonnes.append(cle)
    
    f.close()

    # Écrire le fichier CSV
    f2 = open('SortieCSV_Win.csv', 'w', encoding='utf-8')
    
    # Écrire l'en-tête
    ligneEntete = ",".join(colonnes) + "\n"
    f2.write(ligneEntete)
    
    # Écrire les données
    for evenement in evenements:
        ligne_data = []
        for colonne in colonnes:
            valeur = evenement.get(colonne, "")  # Valeur vide si la colonne n'existe pas
            ligne_data.append(valeur)
        ligne = ";".join(ligne_data) + "\n"
        f2.write(ligne)
    # Écrire le fichier CSV
    f2 = open('SortieCSV_Win.csv', 'w', encoding='utf-8')
    
    # Écrire l'en-tête
    ligneEntete = ";".join(colonnes) + "\n"
    f2.write(ligneEntete)
    
    # Écrire les données
    for evenement in evenements:
        ligne_data = []
        for colonne in colonnes:
            valeur = evenement.get(colonne, "")  # Valeur vide si la colonne n'existe pas
            ligne_data.append(valeur)
        ligne = ";".join(ligne_data) + "\n"
        f2.write(ligne)
    
    f2.close()
    
    print(f"Fichier CSV créé avec {len(evenements)} événements et {len(colonnes)} colonnes")



def open_file(file_path, demande=None):
    f = open(file_path, 'r')
    var_result = []
    var_avantresult = []
    for line in f:
        if ':' in line:
            avantresult = line.split(':', 1)[0].strip()
            result = line.split(':', 1)[1].strip()
            var_avantresult.append(avantresult)
            var_result.append(result)

    if demande is None or demande == "TOUT":
        for res in var_result:
            print(res)
    else:
        i = 0
        for i, res_avant in enumerate(var_avantresult):
            if res_avant == demande:
                print(var_result[i])
            i+=1
    f.close()

def quitter():
    # Ferme la fenêtre principale proprement
    fenetre.destroy()

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Sélectionner un fichier")
fenetre.geometry("850x450")

# Ajout d'un bouton pour ouvrir le dialogue de sélection de fichier
btn_choisir_fichier = tk.Button(fenetre, text="Choisir un fichier", command=choisir_fichier)
btn_choisir_fichier.pack(pady=20)

# Label pour afficher le chemin du fichier
label_chemin = tk.Label(fenetre, text="Aucun fichier sélectionné")
label_chemin.pack(pady=20)

var = tk.StringVar(fenetre)
var.set("Choissir une option") # valeur par défaut
options = ["DTSTAMP", "DTSTART", "DTEND", "SUMMARY", "LOCATION", "DESCRIPTION", "UID", "CREATED","LAST-MODIFIED","SEQUENCE","TOUT"]
MENU = tk.OptionMenu(fenetre, var, *options, command=sauvegarder_choix)
MENU.pack(pady=20)



#Ajout d'un fichier pour afficher le contenue
btn_aff = tk.Button(fenetre,text="Afficher le resultat dans la console", command=lambda: open_file(file, choix))
btn_aff.pack(pady=20)

btn_csvw = tk.Button(fenetre,text="Cree un fichier CSV Pour Windows", command=lambda: csvfileWin(file))
btn_csvw.pack(pady=20)
btn_csvl = tk.Button(fenetre,text="Cree un fichier CSV Pour Linux", command=lambda: csvfileLinux(file))
btn_csvl.pack(pady=20)

# Ajout du bouton "Quitter"
btn_quitter = tk.Button(fenetre, text="Quitter", command=quitter)
btn_quitter.pack(pady=20)

# Lancer l'interface graphique
fenetre.mainloop()