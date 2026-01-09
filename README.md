# 🔒 SAE05 - Analyseur de Trafic Réseau avec Dashboard Web

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/flask-latest-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/license-Educational-orange.svg)](LICENSE)

---

## 📋 Table des Matières

- [Description du Projet](#-description-du-projet)
- [Aperçu Visuel](#-aperçu-visuel)
- [Démarrage Rapide](#-démarrage-rapide)
- [Objectifs Pédagogiques](#-objectifs-pédagogiques)
- [Structure du Projet](#-structure-du-projet)
- [Fonctionnalités Principales](#-fonctionnalités-principales)
- [Installation et Utilisation](#-installation-et-utilisation)
- [Format des Données](#-format-des-données)
- [Détection de Sécurité](#-détection-de-sécurité)
- [Export et Rapports](#-export-et-rapports)
- [Technologies Utilisées](#-technologies-utilisées)
- [Cas d'usage](#-cas-dusage)
- [Dépannage](#-dépannage)
- [FAQ](#-faq)
- [Documentation Associée](#-documentation-associée)
- [Auteur](#-auteur)

---

## 📋 Description du Projet

Ce projet fait partie de la **SAE 1. 05** (Situation d'Apprentissage et d'Évaluation) et se concentre sur l'**analyse et le traitement des données de trafic réseau** capturées via tcpdump.  Le projet permet d'identifier des comportements suspects et de visualiser les données de manière interactive via un dashboard web moderne.

### ✨ Points Forts

- 🖥️ **Interface Graphique Intuitive** : Lanceur avec Tkinter pour une utilisation simplifiée
- 📊 **Dashboard Web Moderne** : Visualisations en temps réel avec Chart.js
- 🛡️ **Détection d'Attaques** :  Identification automatique de scans de ports et SYN floods
- ⚡ **Installation Automatique** : Configuration des dépendances en un clic
- 📁 **Export CSV & Markdown** : Sauvegarde et génération de rapports professionnels
- 📈 **Graphiques Avancés** : Barres, camembert ET radar pour l'analyse des flags TCP

---

## 🖼️ Aperçu Visuel

### Dashboard Web

Le dashboard web affiche **quatre composants principaux** :

1. **Graphique en Barres** : Volume de trafic par adresse IP source (Top 10)
2. **Graphique Radar** : 🆕 Analyse visuelle des flags TCP détectés (S, S., P., F, etc.)
3. **Diagramme Circulaire** : Distribution proportionnelle du trafic réseau
4. **Table d'Alertes** : Liste des comportements suspects détectés avec leur niveau de gravité

### Nouveautés de Visualisation

🆕 **Graphique Radar TCP Flags** : Visualisation multidimensionnelle des différents types de flags TCP détectés dans le trafic (SYN, ACK, PSH, FIN, etc.), permettant d'identifier rapidement les patterns anormaux.

### Interface Graphique de Lancement

L'application principale `lunch.py` offre une interface simple avec :
- Sélection de fichier tcpdump via dialogue
- Option de filtrage du trafic DNS
- Bouton de lancement d'analyse
- Ouverture automatique du dashboard dans le navigateur

---

## 🚀 Démarrage Rapide

### Installation en 3 Étapes

```bash
# 1. Cloner le dépôt
git clone https://github.com/Mathias42lm/SAE05_mathias.git
cd SAE05_mathias

# 2. Naviguer vers le répertoire principal
cd tp

# 3. Lancer l'application (installe automatiquement les dépendances)
python lunch.py
```

### Première Utilisation

1. **Cliquez** sur "📂 Sélectionner un fichier tcpdump"
2. **Choisissez** un fichier de capture (ex: `fichier1000.txt` fourni)
3. **Cochez** "Inclure le trafic DNS" si vous souhaitez analyser le trafic DNS
4. **Cliquez** sur "🚀 LANCER L'ANALYSE"
5. Le **dashboard s'ouvre automatiquement** dans votre navigateur à `http://127.0.0.1:5000`

> 💡 **Astuce** : Des fichiers de test (`fichier182.txt` et `fichier1000.txt`) sont fournis dans le dossier `tp/` pour tester l'application immédiatement.

---

## 🎯 Objectifs Pédagogiques

Ce projet couvre plusieurs compétences techniques et analytiques :

| Domaine | Compétences |
|---------|-------------|
| 📊 **Traitement de Données** | Parsing de fichiers, extraction de métadonnées réseau (IP, ports, flags TCP) |
| 🔒 **Analyse de Sécurité** | Détection d'attaques (scan de ports, SYN flood), identification de comportements suspects |
| 🔄 **Transformation de Données** | Export CSV et Markdown, structuration des données pour analyse |
| 🐍 **Programmation Python** | Structures de données, fonctions, manipulation de fichiers, threading |
| 🌐 **Développement Web** | Création d'un dashboard interactif avec Flask et Chart.js |
| 🖼️ **Interface Graphique** | Développement d'une UI intuitive avec Tkinter |
| 📈 **Visualisation de Données** | Graphiques en barres, radar, diagrammes circulaires, tableaux interactifs |

---

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
│   └── *. ics, *.pdf             # Documents et calendriers
├── tp/                          # Application principale avec interface graphique
│   ├── lunch.py                 # 🚀 Lanceur principal avec GUI Tkinter
│   ├── analyse.py               # Module d'analyse avancé avec détection d'attaques
│   ├── web. py                   # Dashboard web Flask avec visualisations
│   ├── install.py               # Script d'installation des dépendances
│   ├── fichier1000.txt          # Données de test
│   └── fichier182.txt           # Données de test
├── tpexel/                      # Travaux Pratiques Excel/VBA
│   ├── DumpFile.txt             # Fichier de données
│   └── *.pdf                    # Documentation des TPs
├── DumpFile.txt                 # Fichier de capture réseau principal
├── CR. docx                      # Compte-rendu du projet
└── README.md                    # Ce fichier
```

## 🔧 Fonctionnalités Principales

### 1. Application Graphique Complète (`tp/lunch.py`) 🚀

L'application principale offre une interface graphique intuitive pour :
- **Sélection de fichiers** : Dialogue de fichier pour choisir un fichier tcpdump
- **Options de filtrage** : Choix d'inclure ou exclure le trafic DNS
- **Lancement automatique** : Analyse et ouverture automatique du dashboard web
- **Installation automatique** :  Vérification et installation des dépendances

### 2. Dashboard Web Interactif (`tp/web.py`) 📊

Interface web moderne avec visualisations en temps réel : 
- **Graphique en barres** : Volume de trafic par adresse IP source
- **Graphique Radar** : 🆕 Visualisation des flags TCP détectés avec analyse multidimensionnelle
- **Diagramme circulaire (Pie Chart)** : Distribution du trafic pour les 10 IPs les plus actives
- **Table d'alertes** : Liste des comportements suspects détectés
- **Bouton d'export** : 🆕 Génération de rapports Markdown téléchargeables
- **Design moderne** : Interface sombre avec Chart.js pour les graphiques
- **Informations détaillées** : Nombre de paquets, niveau de gravité (HIGH/MID)

### 3. Moteur d'Analyse (`tp/analyse.py`)

Script d'analyse avancé avec fonctionnalités de sécurité :
- **Séparation IP/Port** : Distinction claire entre adresses IP et numéros de ports
- **Détection d'attaques** : 
  - **Scan de ports** : Détecte quand une IP tente d'accéder à plus de 10 services différents
  - **SYN Flood** : Détecte un nombre anormal de paquets SYN (seuil :  25 pour MID, 50 pour HIGH)
- **Analyse des Flags TCP** :  Extraction et comptabilisation de tous les flags TCP
- **Filtrage DNS** : Option pour inclure/exclure le trafic DNS
- **Export CSV** : Génération de fichiers CSV avec toutes les métadonnées
- **Comptage de paquets** : Quantification précise des paquets impliqués dans chaque attaque

### 4. Installation Automatique (`tp/install.py`)

Gestion automatique de l'environnement : 
- **Vérification Flask** : Installation automatique si nécessaire
- **Vérification Tkinter** :  Détection et instructions d'installation
- **Compatibilité Windows** : Support multiplateforme sans emoji dans les messages

---

## 🚀 Installation et Utilisation

### Prérequis

| Logiciel | Version | Installation |
|----------|---------|--------------|
| Python | 3.x | [Télécharger Python](https://www.python.org/downloads/) |
| Flask | Dernière version | Installation automatique via `install.py` |
| Tkinter | Inclus avec Python | Généralement préinstallé (voir section Dépannage) |

### Installation Automatique (Recommandée)

L'application vérifie et installe automatiquement les dépendances nécessaires :

```bash
cd tp
python lunch.py
```

Le script `lunch.py` lance automatiquement `install.py` qui :
1. ✅ Vérifie la présence de Flask et l'installe si nécessaire
2. ✅ Vérifie la présence de Tkinter
3. ✅ Lance l'interface graphique si tout est OK

### Installation Manuelle (Si Nécessaire)

#### Sur Linux/Mac : 
```bash
# Installer Flask
pip install flask

# Si Tkinter n'est pas installé (Ubuntu/Debian)
sudo apt-get install python3-tk

# Autres distributions Linux
# Fedora/RHEL :  sudo dnf install python3-tkinter
# Arch :  sudo pacman -S tk
```

#### Sur Windows :
```bash
# Installer Flask
pip install flask

# Tkinter est généralement inclus avec Python sur Windows
# Si absent, réinstallez Python en cochant "tcl/tk and IDLE"
```

### Utilisation de l'Application Principale

#### Méthode Recommandée :  Interface Graphique

```bash
cd tp
python lunch.py
```

**Workflow étape par étape :**

1. 📂 **Sélectionner un fichier** : Cliquez sur "📂 Sélectionner un fichier tcpdump"
   - Choisissez votre fichier de capture réseau (format texte tcpdump)
   - Exemples fournis : `fichier182.txt`, `fichier1000.txt`

2. ⚙️ **Configurer les options** :  
   - ☑️ Cochez "Inclure le trafic DNS" pour analyser les requêtes DNS (port 53)
   - ☐ Décochez pour exclure le trafic DNS de l'analyse

3. 🚀 **Lancer l'analyse** :  Cliquez sur "🚀 LANCER L'ANALYSE"
   - L'analyse démarre et génère un fichier CSV
   - Le serveur web démarre automatiquement
   - Le dashboard s'ouvre dans votre navigateur par défaut

4. 📊 **Consulter les résultats** : 
   - **Graphique en barres** :  Volume de paquets par IP source
   - **Graphique Radar** : 🆕 Distribution des flags TCP
   - **Diagramme circulaire** :  Top 10 des IPs les plus actives
   - **Table d'alertes** : Attaques détectées avec gravité et nombre de paquets

5. 📥 **Exporter les résultats** : 🆕
   - Cliquez sur "📥 Exporter Rapport (. md)" en haut à droite
   - Télécharge un rapport Markdown formaté avec toutes les données

### Utilisation en Ligne de Commande (Mode Basique)

Pour une utilisation sans interface graphique :

```bash
cd td
python mellier_rendue.py
```

Ce script génère un fichier `resultat_analyse_reseau.csv` avec les paquets analysés (sans détection d'attaques avancée).

### Accès au Dashboard Web

Une fois l'analyse lancée, le dashboard est accessible à : 
```
http://127.0.0.1:5000
```

Le serveur tourne en arrière-plan tant que l'application est ouverte.

---

## 📊 Format des Données

### Entrée (tcpdump)

Les fichiers d'entrée contiennent des captures réseau au format texte tcpdump : 

```
12:34:56.789012 IP 192.168.1.10. 54321 > 10.0.0.1.80:  Flags [S], seq 123456, win 29200, length 0
```

### Sortie (CSV)

Les fichiers CSV générés contiennent les colonnes suivantes :
- **Horodatage** : Timestamp du paquet
- **Source_IP** :  Adresse IP source
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
- **Graphique Radar** : 🆕 Analyse multidimensionnelle des flags TCP (S, S., P., F, R, etc.)
- **Diagramme circulaire (Pie Chart)** : Répartition proportionnelle du trafic entre les 10 IPs principales
- **Table d'alertes** : Liste formatée avec IP, type d'attaque, nombre de paquets, et niveau de gravité

---

## 🔒 Détection de Sécurité

Le module `analyse.py` implémente deux types de détection d'attaques réseau avec seuils configurables :

### 🔍 1. Scan de Ports

**Description** : Détecte les tentatives de reconnaissance réseau où une IP tente d'identifier les services actifs.

| Métrique | Valeur | Niveau |
|----------|--------|--------|
| **Seuil de Détection** | > 10 ports différents | ALERTE |
| **Niveau MID** | 10-39 ports différents | 🟠 MOYEN |
| **Niveau HIGH** | ≥ 40 ports différents | 🔴 ÉLEVÉ |

**Indicateurs** :
- Multiples connexions vers des ports/services différents depuis une même IP
- Tentative de cartographie du réseau
- Comptage du nombre total de paquets envoyés durant le scan

**Exemple d'Alerte** : 
```
IP: 192.168.1.100
Type:  Scan de Ports
Paquets:  45
Niveau: HIGH
Détails:  Scan sur 42 ports (45 paquets)
```

### 💥 2. SYN Flood

**Description** : Détecte les attaques par déni de service (DoS) basées sur l'envoi massif de paquets SYN.

| Métrique | Valeur | Niveau |
|----------|--------|--------|
| **Seuil MID** | ≥ 25 paquets SYN | 🟠 MOYEN |
| **Seuil HIGH** | ≥ 50 paquets SYN | 🔴 ÉLEVÉ |

**Indicateurs** :
- Volume anormal de paquets avec flag TCP `[S]`
- Même IP source génère de nombreuses tentatives de connexion
- Peut saturer la table des connexions de la cible

**Exemple d'Alerte** :
```
IP: 10.0.0.55
Type: SYN Flood
Paquets: 67
Niveau: HIGH
Détails: Attaque par inondation (67 paquets SYN)
```

### 📋 Affichage des Alertes dans le Dashboard

Les alertes sont présentées sous forme de tableau avec : 

| Colonne | Description |
|---------|-------------|
| **IP Source** | Adresse IP à l'origine de l'activité suspecte |
| **Type** | "Scan de Ports" ou "SYN Flood" |
| **Paquets** | Quantité exacte de paquets impliqués |
| **Gravité** | Badge coloré :  🔴 HIGH (rouge) ou 🟠 MID (orange) |

### ⚙️ Configuration des Seuils

Les seuils de détection peuvent être ajustés dans `tp/analyse.py` dans la fonction `detecter_attaques()` :

```python
# Seuils configurables (section --- SEUILS ---)
LIMIT_SYN_HIGH = 50                        # SYN Flood niveau HIGH
LIMIT_SYN_MID = LIMIT_SYN_HIGH / 2         # SYN Flood niveau MID (calculé:  25)
LIMIT_SCAN_PORTS = 10                      # Scan de ports détection
LIMIT_SCAN_MAX = LIMIT_SCAN_PORTS + 30     # Scan de ports niveau HIGH (calculé: 40)
```

**Note** : Les valeurs `LIMIT_SYN_MID` et `LIMIT_SCAN_MAX` sont calculées automatiquement.  Modifiez `LIMIT_SYN_HIGH` et `LIMIT_SCAN_PORTS` pour ajuster les seuils. 

---

## 📥 Export et Rapports

### 🆕 Export Markdown

Le dashboard propose désormais un **système d'export de rapports** au format Markdown :

#### Accès à l'Export

Dans le dashboard web (`http://127.0.0.1:5000`), cliquez sur le bouton : 
```
📥 Exporter Rapport (. md)
```

#### Contenu du Rapport

Le fichier `rapport_securite.md` généré contient : 

1. **📊 Top 10 IP par Volume**
   - Tableau complet des adresses IP les plus actives
   - Nombre de paquets pour chaque IP

2. **🚩 Analyse des Flags TCP**
   - Liste détaillée de tous les flags TCP détectés
   - Comptage pour chaque type de flag (S, S., P., F, R, etc.)

3. **⚠️ Alertes de Sécurité**
   - Tableau des comportements suspects
   - IP source, type d'attaque, et niveau de gravité

#### Exemple de Structure du Rapport

```markdown
# 🛡️ Rapport d'Analyse Réseau

## 📊 Top 10 IP par Volume
| Adresse IP | Nombre de Paquets |
| :--- | :--- |
| 192.168.1.100 | 156 |
| 10.0.0.55 | 89 |

## 🚩 Analyse des Flags TCP
* **S**:  234 paquets
* **S. **: 189 paquets
* **P.**: 567 paquets

## ⚠️ Alertes de Sécurité
| IP Source | Type d'Alerte | Gravité |
| :--- | : --- | :--- |
| 192.168.1.100 | Scan de Ports | HIGH |
| 10.0.0.55 | SYN Flood | MID |
```

#### Cas d'Usage du Rapport

- 📝 **Documentation** : Archivage des analyses pour référence future
- 🔗 **Intégration** : Import dans des wikis, GitLab/GitHub Issues
- 📊 **Présentation** : Conversion facile en PDF via Pandoc ou éditeurs Markdown
- 📧 **Partage** :  Envoi par email avec formatage préservé

---

## 🎨 Technologies Utilisées

| Technologie | Usage | Version |
|-------------|-------|---------|
| ![Python](https://img.shields.io/badge/Python-3.x-blue? logo=python) | Langage principal | 3.x |
| ![Tkinter](https://img.shields.io/badge/Tkinter-GUI-orange) | Interface graphique lanceur | Inclus |
| ![Flask](https://img.shields.io/badge/Flask-Web-green? logo=flask) | Framework web pour dashboard | Dernière |
| ![Chart.js](https://img.shields.io/badge/Chart.js-Viz-yellow) | Graphiques interactifs (Bar, Pie, Radar) | CDN |
| ![CSV](https://img.shields.io/badge/CSV-Export-lightgrey) | Format d'export de données | Standard |
| ![Markdown](https://img.shields.io/badge/Markdown-Rapport-blue) | 🆕 Format de rapport exportable | Standard |
| ![Threading](https://img.shields.io/badge/Threading-Async-purple) | Exécution parallèle du serveur | Python std |

### Architecture Logicielle

```
┌─────────────────┐
│   lunch.py      │  ← Interface Graphique (Tkinter)
│   (Lanceur)     │
└────────┬────────┘
         │
         ├─→ ┌──────���──────┐
         │   │ install.py  │  ← Vérification des dépendances
         │   └─────────────┘
         │
         ├─→ ┌─────────────────┐
         │   │   analyse.py    │  ← Parsing & Détection d'attaques
         │   └─────────────────┘
         │
         └─→ ┌─────────────────┐
             │     web.py      │  ← Serveur Flask + Dashboard
             └─────────────────┘
                     │
                     ├─→ Chart.js (Graphiques:  Bar, Pie, Radar)
                     ├─→ HTML/CSS (Interface)
                     └─→ /export (Génération Markdown)
```

---

## 💼 Cas d'usage

### Cas d'Usage 1 : Analyse de Sécurité Réseau

**Contexte** : Vous êtes administrateur réseau et suspectez une activité anormale. 

**Étapes** :
1. Capturez le trafic réseau avec tcpdump :  `sudo tcpdump -i eth0 -w capture.txt`
2. Lancez l'application : `python lunch.py`
3. Sélectionnez le fichier `capture.txt`
4. Analysez les alertes dans le dashboard
5. 🆕 Exportez le rapport Markdown pour documentation
6. Exportez les données CSV pour analyse approfondie

**Résultat** : Identification rapide des IPs suspectes et génération de rapports professionnels.

### Cas d'Usage 2 :  Étude du Trafic Réseau

**Contexte** : Projet académique d'analyse de trafic réseau.

**Étapes** : 
1. Utilisez les fichiers de test fournis (`fichier1000.txt`)
2. Expérimentez avec/sans filtrage DNS
3. Analysez les visualisations (volume, distribution, flags TCP)
4. 🆕 Utilisez le graphique radar pour comprendre les patterns de flags
5. Exportez les données CSV et Markdown pour traitement dans Excel/Python

**Résultat** :  Compréhension des patterns de trafic et apprentissage de l'analyse réseau.

### Cas d'Usage 3 : Détection d'Intrusion

**Contexte** :  Formation en cybersécurité, simulation d'attaques.

**Étapes** :
1. Générez du trafic de scan de ports (nmap, netcat)
2. Capturez avec tcpdump
3. Analysez avec l'application
4. Observez les détections HIGH/MID dans le dashboard
5. 🆕 Générez un rapport Markdown pour documentation de l'incident

**Résultat** :  Apprentissage des techniques de détection d'intrusion avec documentation professionnelle.

### Cas d'Usage 4 : Monitoring Réseau Continu

**Contexte** :  Surveillance du trafic sur une période donnée.

**Étapes** :
1. Configurez tcpdump en rotation de fichiers
2. Analysez chaque fichier avec l'application
3. Comparez les CSV et rapports Markdown générés pour identifier les tendances
4. Archivez les analyses pour audit

**Résultat** :  Historique du trafic et détection de patterns anormaux avec traçabilité.

---

## 🔧 Dépannage

### ❌ Problème :  "Tkinter n'est pas détecté"

**Solution Linux (Ubuntu/Debian)** :
```bash
sudo apt-get update
sudo apt-get install python3-tk
```

**Solution Linux (Fedora/RHEL)** :
```bash
sudo dnf install python3-tkinter
```

**Solution Mac** :
```bash
# Réinstaller Python avec Homebrew
brew install python-tk
```

**Solution Windows** :
- Réinstallez Python depuis [python.org](https://www.python.org/downloads/)
- Cochez l'option "tcl/tk and IDLE" lors de l'installation

### ❌ Problème : "Flask n'est pas détecté après installation"

**Causes possibles** :
- Multiples versions de Python installées
- Problèmes de PATH

**Solutions** :
```bash
# Vérifier quelle version de pip est utilisée
pip --version

# Installer Flask avec pip3 explicitement
pip3 install flask

# Ou utiliser python -m pip
python -m pip install flask
```

### ❌ Problème : Le dashboard ne s'ouvre pas automatiquement

**Solutions** :
1. Ouvrez manuellement votre navigateur
2. Allez à l'adresse :  `http://127.0.0.1:5000`
3. Si le port 5000 est occupé, modifiez dans `web.py` dans la fonction `start_server()` :
   ```python
   app.run(host='0.0.0.0', port=5001, debug=False, use_reloader=False)
   ```

### ❌ Problème : "Erreur lors du parsing du fichier"

**Vérifications** :
- Le fichier est-il au format texte tcpdump ?
- Le fichier contient-il des lignes valides ?
- Exemple de format attendu : 
  ```
  15:34:04.766656 IP 192.168.1.10.80 > 192.168.1.20.50019: Flags [S], seq 123456
  ```

**Solution** :
```bash
# Générer une capture valide avec tcpdump
sudo tcpdump -i eth0 -n > capture.txt
# Attendez quelques secondes puis Ctrl+C
```

### ❌ Problème :  Fichier CSV vide ou incomplet

**Causes** :
- Fichier source mal formaté
- Filtrage DNS trop restrictif
- Données hexadécimales non filtrées

**Solution** :
- Vérifiez que le fichier contient des lignes commençant par un horodatage
- Désactivez le filtrage DNS si nécessaire
- Consultez les exemples fournis (`fichier182.txt`, `fichier1000.txt`)

### ❌ Problème : L'export Markdown ne se télécharge pas

**Solutions** :
1. Vérifiez que votre navigateur autorise les téléchargements
2. Essayez un autre navigateur (Chrome, Firefox, Edge)
3. Vérifiez les autorisations de téléchargement dans les paramètres du navigateur
4. Le fichier est automatiquement nommé `rapport_securite.md`

### ❌ Problème :  "Permission denied" lors de l'installation

**Solution** :
```bash
# Linux/Mac :  Utiliser --user
pip install --user flask

# Ou installer dans un environnement virtuel
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install flask
```

---

## ❓ FAQ

### Q1 : Quels formats de fichiers sont supportés ? 

**R :** L'application supporte les fichiers texte générés par `tcpdump` avec des lignes au format :
```
HH:MM:SS.microsec IP source. port > dest.port: Flags [X], ... 
```

### Q2 : Puis-je analyser des fichiers . pcap binaires ?

**R :** Non, l'application nécessite des fichiers texte.  Convertissez d'abord avec : 
```bash
tcpdump -r fichier.pcap -n > fichier.txt
```

### Q3 :  Combien de lignes de trafic l'application peut-elle traiter ?

**R :** L'application a été testée avec des fichiers contenant jusqu'à 1000+ lignes.  Pour des fichiers très volumineux (>10 000 lignes), le chargement peut prendre quelques secondes.

### Q4 : Les alertes sont-elles fiables à 100% ?

**R :** Les alertes sont basées sur des seuils configurables et des heuristiques. Elles peuvent générer des **faux positifs** (trafic légitime détecté comme suspect) et des **faux négatifs** (attaques non détectées). Utilisez-les comme indicateurs à vérifier manuellement.

### Q5 : Puis-je ajuster les seuils de détection ?

**R :** Oui !  Éditez le fichier `tp/analyse.py` dans la fonction `detecter_attaques()`, section `--- SEUILS ---` : 
```python
LIMIT_SYN_HIGH = 50                        # Votre valeur
LIMIT_SYN_MID = LIMIT_SYN_HIGH / 2         # Calculé automatiquement
LIMIT_SCAN_PORTS = 10                      # Votre valeur
LIMIT_SCAN_MAX = LIMIT_SCAN_PORTS + 30     # Calculé automatiquement
```

**Astuce** : Modifiez uniquement `LIMIT_SYN_HIGH` et `LIMIT_SCAN_PORTS`. Les autres valeurs sont calculées automatiquement.

### Q6 : Le dashboard est-il accessible depuis un autre ordinateur ?

**R :** Par défaut, le serveur écoute sur `0.0.0.0:5000`, ce qui le rend accessible depuis le réseau local.  Accédez via `http://<IP_SERVEUR>:5000` depuis un autre appareil.  

⚠️ **Attention** : N'exposez pas ce serveur sur Internet sans sécurisation appropriée. 

### Q7 : Où sont stockés les fichiers générés ?

**R :** 
- **CSV** : `tp/resultat_analyse.csv` (écrasé à chaque analyse)
- **Markdown** : Téléchargé via le navigateur sous le nom `rapport_securite.md`

### Q8 : L'application fonctionne-t-elle hors ligne ?

**R :** Partiellement. L'application nécessite une connexion Internet pour charger Chart.js depuis le CDN lors de l'ouverture du dashboard.  Les autres fonctionnalités (parsing, export CSV/MD) fonctionnent hors ligne.

### Q9 : Puis-je utiliser l'application sur un serveur sans interface graphique ?

**R :** Oui ! Utilisez directement le module d'analyse en ligne de commande :
```bash
cd tp
python3 -c "import analyse; \
data, alerts = analyse.parse_tcpdump_flexible('fichier.txt', 'output.csv'); \
print(f'{len(data)} paquets, {len(alerts)} alertes')"
```

### Q10 : À quoi sert le graphique radar ?

**R :** 🆕 Le graphique radar permet de visualiser **la distribution des différents flags TCP** dans le trafic réseau.  Chaque axe représente un type de flag (S, S., P., F, R, etc.). Cette visualisation multidimensionnelle aide à : 
- Identifier rapidement les patterns anormaux
- Détecter des anomalies dans la distribution des flags
- Comprendre les types de communication dominants

### Q11 : Comment contribuer au projet ?

**R :** Ce projet est à but éducatif.  Pour des améliorations, contactez l'auteur ou créez un fork du dépôt. 

---

## 📚 Documentation Associée

Le projet inclut plusieurs documents pédagogiques dans les différents répertoires :

| Document | Localisation | Description |
|----------|--------------|-------------|
| `SAE-105-. pdf` | `/td/` | Cahier des charges du projet SAE 1. 05 |
| `TP2 - SAE1.05.pdf` | `/tpexel/` | Instructions pour les travaux pratiques |
| `SAE1.05 - Excel.pdf` | `/tpexel/` | Documentation pour la partie Excel |
| `SAE1.05 - VBA.pdf` | `/tpexel/` | Documentation pour la partie VBA |
| `CR. docx` | `/` | Compte-rendu du projet |
| `tcpdump. docx` | `/tp/` et `/td/` | Documentation sur tcpdump |

---

## 👨‍💻 Auteur

**Mathias** - SAE 1.05  
🔗 [GitHub Repository](https://github.com/Mathias42lm/SAE05_mathias)

---

## 📝 Notes Techniques

### Conventions et Détails d'Implémentation

- ✅ Les fichiers CSV sont automatiquement ignorés par git (voir `.gitignore`)
- ✅ Les données hexadécimales dans les captures sont automatiquement filtrées lors du parsing
- ✅ Le projet supporte à la fois les noms d'hôtes et les adresses IP dans les captures tcpdump
- ✅ Le serveur web Flask écoute par défaut sur `http://0.0.0.0:5000` (accessible réseau local)
- ✅ L'installation des dépendances est entièrement automatisée pour simplifier le déploiement
- ✅ Compatible Windows, Linux et macOS
- ✅ Les graphiques sont générés dynamiquement à partir des données analysées en temps réel
- ✅ 🆕 Le graphique radar utilise Chart.js pour une visualisation multidimensionnelle des flags TCP
- ✅ Le diagramme circulaire utilise une palette de 10 couleurs distinctes pour meilleure lisibilité
- ✅ Le serveur web tourne dans un thread séparé pour ne pas bloquer l'interface Tkinter
- ✅ Ouverture automatique du navigateur avec un délai de 1.5s pour laisser le serveur démarrer
- ✅ 🆕 Export Markdown avec formatage optimisé pour GitHub, GitLab et conversion PDF

### Limitations Connues

- 📌 Le dashboard nécessite une connexion Internet pour charger Chart.js (CDN)
- 📌 Les fichiers très volumineux (>100 000 lignes) peuvent ralentir l'analyse
- 📌 Le parsing ne supporte que le format texte tcpdump (pas les fichiers . pcap binaires)
- 📌 Un seul fichier CSV est conservé à la fois (écrasement à chaque nouvelle analyse)
- 📌 Le serveur web n'a pas d'authentification (usage local uniquement)

### Améliorations Futures Potentielles

- 🚀 Support des fichiers . pcap via la bibliothèque Scapy
- 🚀 Détection d'autres types d'attaques (DDoS, ARP Spoofing, etc.)
- 🚀 Historique des analyses avec graphiques d'évolution temporelle
- 🚀 Export PDF des rapports d'analyse avec Chart.js intégré
- 🚀 Mode monitoring en temps réel avec refresh automatique
- 🚀 Interface web pour uploader des fichiers sans Tkinter
- 🚀 Support de filtres avancés (par IP, par port, par protocole)
- 🚀 Intégration avec des bases de données pour stockage persistant
- 🚀 Export JSON pour intégration avec des SIEM

---

## 📄 Licence

Ce projet est développé dans un cadre éducatif (SAE 1.05). Usage libre pour l'apprentissage et la formation.

---

## 🙏 Remerciements

Merci aux enseignants et encadrants de la SAE 1.05 pour le support et les ressources pédagogiques. 

---

<div align="center">

**⭐ Si ce projet vous a été utile, n'hésitez pas à le mettre en favoris !  ⭐**

Made with ❤️ for learning cybersecurity and network analysis

</div>
