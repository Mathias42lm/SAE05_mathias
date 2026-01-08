import install
if (install.verifier_et_configurer() == 1):
    import tkinter as tk
    from tkinter import filedialog, messagebox
    import threading
    import webbrowser
    import analyse as Analyse  # Assure-toi que le fichier s'appelle Analyse.py
    import web      # Assure-toi que le fichier s'appelle web.py
else:
    import sys
    sys.exit(1)
# Variables globales
chemin_fichier_source = None

def choisir_fichier():
    global chemin_fichier_source
    chemin = filedialog.askopenfilename(title="Sélectionner un log TCPDump", 
                                       filetypes=[("Fichiers texte", "*.txt"), ("Tous les fichiers", "*.*")])
    if chemin:
        label_chemin.config(text=f"Fichier : {chemin}")
        chemin_fichier_source = chemin

def lancer_programme():
    global chemin_fichier_source
    if not chemin_fichier_source:
        messagebox.showwarning("Attention", "Veuillez d'abord choisir un fichier !")
        return

    # Récupération de l'option du filtre DNS
    garder_dns = var_dns.get()
    fichier_csv = "resultat_analyse.csv"

    try:
        # 1. Lancer l'analyse (Analyse.py)
        donnees, alertes = Analyse.parse_tcpdump_flexible(
            chemin_fichier_source, 
            fichier_csv, 
            garder_domain=garder_dns
        )

        if not donnees:
            messagebox.showerror("Erreur", "Le fichier est vide ou invalide.")
            return

        # 2. Lancer le serveur Web dans un thread séparé
        web_thread = threading.Thread(target=web.start_server, args=(donnees, alertes), daemon=True)
        web_thread.start()

        # --- CORRECTION ICI ---
        # On utilise 'fenetre.after' au lieu de 'tk.after'
        fenetre.after(1500, lambda: webbrowser.open("http://127.0.0.1:5000"))
        
        messagebox.showinfo("Succès", "Analyse terminée ! Le tableau de bord s'ouvre dans votre navigateur.")

    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur est survenue : {e}")

# --- Interface Graphique ---
fenetre = tk.Tk()
fenetre.title("TCPDump Analyzer")
fenetre.geometry("500x450")

tk.Label(fenetre, text="Analyseur de Trafic Réseau", font=("Arial", 16, "bold")).pack(pady=20)

btn_choisir = tk.Button(fenetre, text="📂 Sélectionner un fichier TCPDump", command=choisir_fichier, width=30)
btn_choisir.pack(pady=10)

label_chemin = tk.Label(fenetre, text="Aucun fichier sélectionné", fg="grey")
label_chemin.pack(pady=5)

var_dns = tk.BooleanVar(value=False)
check_dns = tk.Checkbutton(fenetre, text="Inclure le trafic DNS (port 53 / domain)", variable=var_dns)
check_dns.pack(pady=15)

btn_lancer = tk.Button(fenetre, text="🚀 LANCER L'ANALYSE", command=lancer_programme, 
                       bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), width=25, height=2)
btn_lancer.pack(pady=20)

tk.Button(fenetre, text="Quitter", command=fenetre.destroy, width=15).pack(pady=20)

fenetre.mainloop()
