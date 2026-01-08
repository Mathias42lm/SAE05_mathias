import subprocess
import sys

def installer_package(package):
    """Installe un package Python via pip."""
    print(f"--- Installation de {package} en cours...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"✅ {package} a été installé avec succès.")
    except subprocess.CalledProcessError:
        print(f"❌ Erreur lors de l'installation de {package}.")

def verifier_et_configurer():
    print("=== Configuration automatique de l'environnement ===\n")

    # 1. Vérification de Flask (nécessaire pour web.py)
    try:
        import flask
        print("✅ Flask est déjà installé.")
    except ImportError:
        installer_package("flask")

    try:
        import flask
    except ImportError:
        print("⚠️ Flask n'est pas détecté.")
        print("Sur Linux, utilisez : sudo apt-get install python3-flask")
        return 0
    

    # 2. Vérification de Tkinter (souvent inclus, mais parfois séparé sur Linux)
    try:
        import tkinter
        print("✅ Tkinter est disponible.")
    except ImportError:
        print("⚠️ Tkinter n'est pas détecté.")
        print("Sur Linux, utilisez : sudo apt-get install python3-tk")
        return 0

    print("\n" + "="*45)
    print("L'environnement est prêt !")
    print("="*45)
    return 1