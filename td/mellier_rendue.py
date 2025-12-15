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
fenetre.geometry("800x400")

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

# Ajout du bouton "Quitter"
btn_quitter = tk.Button(fenetre, text="Quitter", command=quitter)
btn_quitter.pack(pady=20)

# Lancer l'interface graphique
fenetre.mainloop()


