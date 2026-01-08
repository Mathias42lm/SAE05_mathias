# SAE05 - Analyseur de Trafic Réseau avec Dashboard Web

## 📋 Description du Projet

Ce projet fait partie de la SAE 1.05 (Situation d'Apprentissage et d'Évaluation) et se concentre sur l'analyse et le traitement des données de trafic réseau capturées via tcpdump. Le projet utilise Python pour parser, analyser et détecter des comportements suspects dans les captures réseau, avec une interface graphique et un dashboard web interactif pour visualiser les résultats.

## 🎯 Objectifs Pédagogiques

Ce projet couvre plusieurs compétences :
- **Lecture et traitement de données** : parsing de fichiers de capture réseau
- **Extraction de données** : extraction de métadonnées réseau (IP, ports, flags TCP, etc.)
- **Analyse de sécurité** : détection d'attaques (scan de ports, SYN flood)
- **Transformation de données** : export au format CSV pour analyse ultérieure
- **Programmation Python** : utilisation de structures de données, fonctions, et manipulation de fichiers
- **Développement Web** : création d'un dashboard interactif avec Flask et Chart.js
- **Interface Graphique** : développement d'une interface utilisateur avec Tkinter
- **Visualisation de données** : graphiques en barres et diagrammes circulaires (pie chart)

## 📁 Structure du Projet

```
SAE05_mathias/
├── td/                          # Travaux Dirigés
│   ├── mellier_rendue.py        # Script d'analyse réseau (version de base)
│   ├── fichier182.txt           # Fichier de données tcpdump
│   ├── fichier1000.txt          # Fichier de données tcpdump
│   ├── boiteDialogue.py         # Interface de dialogue
│   ├── ecritureCSV.py           # Module d'écriture CSV
│   ├── Aide organisation.txt    # Notes d'organisation du projet
│   └── *.ics, *.pdf             # Documents et calendriers
├── tp/                          # Application principale avec interface graphique
│   ├── lunch.py                 # 🚀 Lanceur principal avec GUI Tkinter
│   ├── analyse.py               # Module d'analyse avancé avec détection d'attaques
│   ├── web.py                   # Dashboard web Flask avec visualisations
│   ├── install.py               # Script d'installation des dépendances
│   ├── fichier1000.txt          # Données de test
│   └── fichier182.txt           # Données de test
├── tpexel/                      # Travaux Pratiques Excel/VBA
│   ├── DumpFile.txt             # Fichier de données
│   └── *.pdf                    # Documentation des TPs
├── DumpFile.txt                 # Fichier de capture réseau principal
├── CR.docx                      # Compte-rendu du projet
└── README.md                    # Ce fichier
```

## 🔧 Fonctionnalités Principales

### 1. Application Graphique Complète (`tp/lunch.py`) 🚀

L'application principale offre une interface graphique intuitive pour :
- **Sélection de fichiers** : Dialogue de fichier pour choisir un fichier TCPDump
- **Options de filtrage** : Choix d'inclure ou exclure le trafic DNS
- **Lancement automatique** : Analyse et ouverture automatique du dashboard web
- **Installation automatique** : Vérification et installation des dépendances

### 2. Dashboard Web Interactif (`tp/web.py`) 📊

Interface web moderne avec visualisations en temps réel :
- **Graphique en barres** : Volume de trafic par adresse IP source
- **Diagramme circulaire (Pie Chart)** : Distribution du trafic pour les 10 IPs les plus actives
- **Table d'alertes** : Liste des comportements suspects détectés
- **Design moderne** : Interface sombre avec Chart.js pour les graphiques
- **Informations détaillées** : Nombre de paquets, niveau de gravité (HIGH/MID)

### 3. Moteur d'Analyse (`tp/analyse.py`)

Script d'analyse avancé avec fonctionnalités de sécurité :
- **Séparation IP/Port** : Distinction claire entre adresses IP et numéros de ports
- **Détection d'attaques** :
  - **Scan de ports** : Détecte quand une IP tente d'accéder à plus de 10 services différents
  - **SYN Flood** : Détecte un nombre anormal de paquets SYN (seuil : 25 pour MID, 50 pour HIGH)
- **Filtrage DNS** : Option pour inclure/exclure le trafic DNS
- **Export CSV** : Génération de fichiers CSV avec toutes les métadonnées
- **Comptage de paquets** : Quantification précise des paquets impliqués dans chaque attaque

### 4. Installation Automatique (`tp/install.py`)

Gestion automatique de l'environnement :
- **Vérification Flask** : Installation automatique si nécessaire
- **Vérification Tkinter** : Détection et instructions d'installation
- **Compatibilité Windows** : Support multiplateforme sans emoji dans les messages

## 🚀 Installation et Utilisation

### Prérequis

```bash
Python 3.x
Flask (installation automatique via install.py)
Tkinter (généralement inclus avec Python)
```

### Installation Automatique

L'application vérifie et installe automatiquement les dépendances nécessaires :

```bash
cd /home/runner/work/SAE05_mathias/SAE05_mathias/tp
python lunch.py
```

Le script `lunch.py` lance automatiquement `install.py` qui :
1. Vérifie la présence de Flask et l'installe si nécessaire
2. Vérifie la présence de Tkinter
3. Lance l'interface graphique si tout est OK

### Installation Manuelle (si nécessaire)

#### Sur Linux/Mac :
```bash
pip install flask
# Si Tkinter n'est pas installé :
sudo apt-get install python3-tk  # Debian/Ubuntu
```

#### Sur Windows :
```bash
pip install flask
# Tkinter est généralement inclus avec Python sur Windows
```

### Utilisation de l'Application Principale

#### Méthode Recommandée : Interface Graphique

```bash
cd /home/runner/work/SAE05_mathias/SAE05_mathias/tp
python lunch.py
```

1. Cliquez sur "📂 Sélectionner un fichier TCPDump"
2. Choisissez votre fichier de capture (ex: `fichier1000.txt`)
3. Cochez "Inclure le trafic DNS" si souhaité
4. Cliquez sur "🚀 LANCER L'ANALYSE"
5. Le dashboard web s'ouvre automatiquement dans votre navigateur

Le dashboard affiche :
- **Graphique en barres** : Volume de paquets par IP
- **Diagramme circulaire** : Top 10 des IPs les plus actives
- **Table d'alertes** : Attaques détectées avec gravité et nombre de paquets

### Utilisation en Ligne de Commande

Pour une utilisation basique sans interface graphique :

```bash
cd /home/runner/work/SAE05_mathias/SAE05_mathias/td
python mellier_rendue.py
```

Ce script génère un fichier `resultat_analyse_reseau.csv` avec les paquets analysés.

## 📊 Format des Données

### Entrée (tcpdump)

Les fichiers d'entrée contiennent des captures réseau au format texte tcpdump :

```
12:34:56.789012 IP 192.168.1.10.54321 > 10.0.0.1.80: Flags [S], seq 123456, win 29200, length 0
```

### Sortie (CSV)

Les fichiers CSV générés contiennent les colonnes suivantes :
- **Horodatage** : Timestamp du paquet
- **Source_IP** : Adresse IP source
- **Source_Port** : Port source
- **Dest_IP** : Adresse IP destination
- **Dest_Port** : Port destination
- **Flags** : Flags TCP (S, S., P., etc.)
- **Sequence** : Numéro de séquence TCP
- **Acknowledgment** : Numéro d'acquittement TCP
- **Window** : Taille de fenêtre TCP
- **Length** : Longueur des données

### Visualisations Web

Le dashboard web génère automatiquement :
- **Graphique en barres** : Top 10 des IPs sources par volume de paquets
- **Diagramme circulaire (Pie Chart)** : Répartition proportionnelle du trafic entre les 10 IPs principales
- **Table d'alertes** : Liste formatée avec IP, type d'attaque, nombre de paquets, et niveau de gravité

## 🔒 Détection de Sécurité

Le module `analyse.py` implémente deux types de détection d'attaques avec seuils configurables :

### Scan de Ports
- **Seuil de détection** : Plus de 10 ports/services différents contactés
- **Seuil MID** : Entre 10 et 40 ports différents
- **Seuil HIGH** : Plus de 40 ports différents
- **Indicateur** : Tentative de reconnaissance du réseau
- **Comptage** : Nombre total de paquets envoyés durant le scan

### SYN Flood
- **Seuil MID** : Plus de 25 paquets SYN depuis une même IP
- **Seuil HIGH** : Plus de 50 paquets SYN depuis une même IP
- **Indicateur** : Tentative de déni de service (DoS)
- **Comptage** : Nombre de paquets SYN détectés

### Affichage des Alertes

Les alertes sont présentées dans le dashboard web avec :
- **IP Source** : Adresse IP à l'origine de l'activité suspecte
- **Type d'Attaque** : "Scan de Ports" ou "SYN Flood"
- **Nombre de Paquets** : Quantité exacte de paquets impliqués
- **Niveau de Gravité** : Badge coloré (HIGH en rouge, MID en orange)

## 🎨 Technologies Utilisées

- **Python 3.x** : Langage principal
- **Tkinter** : Interface graphique pour le lanceur
- **Flask** : Framework web pour le dashboard
- **Chart.js** : Bibliothèque JavaScript pour les graphiques interactifs
- **CSV** : Format d'export des données
- **Threading** : Exécution parallèle du serveur web

## 📚 Documentation Associée

Le projet inclut plusieurs documents pédagogiques :
- `SAE-105-.pdf` : Cahier des charges du projet
- `TP2 - SAE1.05.pdf` : Instructions pour les travaux pratiques
- `SAE1.05 - Excel.pdf` et `SAE1.05 - VBA.pdf` : Documentation pour la partie Excel/VBA
- `CR.docx` : Compte-rendu du projet

## 👨‍💻 Auteur

Mathias - SAE 1.05

## 📝 Notes Techniques

- Les fichiers CSV sont ignorés par git (voir `.gitignore`)
- Les données hexadécimales sont automatiquement filtrées lors du parsing
- Le projet supporte les noms d'hôtes et les adresses IP dans les captures
- Le serveur web Flask tourne sur `http://127.0.0.1:5000`
- L'installation des dépendances est automatisée pour plus de simplicité
- Compatible Windows (suppression des emojis dans install.py pour éviter les erreurs d'encodage)
- Les graphiques sont générés dynamiquement à partir des données analysées
- Le dashboard utilise une palette de 10 couleurs pour le diagramme circulaire
