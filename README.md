# SAE05 - Analyse du Trafic Réseau

## 📋 Description du Projet

Ce projet fait partie de la SAE 1.05 (Situation d'Apprentissage et d'Évaluation) et se concentre sur l'analyse et le traitement des données de trafic réseau capturées via tcpdump. Le projet utilise Python pour parser, analyser et détecter des comportements suspects dans les captures réseau.

## 🎯 Objectifs Pédagogiques

Ce projet couvre plusieurs compétences :
- **Lecture et traitement de données** : parsing de fichiers de capture réseau
- **Extraction de données** : extraction de métadonnées réseau (IP, ports, flags TCP, etc.)
- **Analyse de sécurité** : détection d'attaques (scan de ports, SYN flood)
- **Transformation de données** : export au format CSV pour analyse ultérieure
- **Programmation Python** : utilisation de structures de données, fonctions, et manipulation de fichiers

## 📁 Structure du Projet

```
SAE05_mathias/
├── td/                          # Travaux Dirigés
│   ├── mellier_rendue.py        # Script d'analyse réseau (version de base)
│   ├── fichier182.txt           # Fichier de données tcpdump
│   ├── fichier1000.txt          # Fichier de données tcpdump
│   ├── Aide organisation.txt    # Notes d'organisation du projet
│   └── *.ics, *.pdf             # Documents et calendriers
├── testpython/                  # Scripts de test et analyse
│   ├── analyse.py               # Script d'analyse avancé avec détection d'attaques
│   ├── fichier1000.txt          # Données de test
│   └── fichier182.txt           # Données de test
├── tpexel/                      # Travaux Pratiques Excel/VBA
│   ├── DumpFile.txt             # Fichier de données
│   └── *.pdf                    # Documentation des TPs
└── README.md                    # Ce fichier
```

## 🔧 Fonctionnalités Principales

### 1. Script d'Analyse de Base (`td/mellier_rendue.py`)

Ce script parse les fichiers de capture tcpdump et extrait les informations suivantes :
- **Horodatage** : timestamp de chaque paquet
- **Protocole** : type de protocole (IP)
- **Source_Port** : IP source et port
- **Destination_Port** : IP destination et port
- **Flags TCP** : flags de connexion (SYN, ACK, etc.)
- **Sequence, Acknowledgment, Window, Length** : métadonnées TCP

**Sortie** : Fichier CSV avec les données parsées

### 2. Script d'Analyse Avancé (`testpython/analyse.py`)

Version améliorée avec fonctionnalités supplémentaires :
- **Séparation IP/Port** : distinction claire entre adresses IP et numéros de ports
- **Détection d'attaques** :
  - **Scan de ports** : détecte quand une IP tente d'accéder à plus de 10 services différents
  - **SYN Flood** : détecte un nombre anormal de paquets SYN depuis une même source
- **Filtrage DNS** : option pour inclure/exclure le trafic DNS
- **Rapport de sécurité** : génération automatique d'alertes

## 🚀 Installation et Utilisation

### Prérequis

```bash
Python 3.x
Module csv (inclus dans Python standard)
Module os (inclus dans Python standard)
```

### Utilisation

#### Analyse de Base

```bash
cd /home/runner/work/SAE05_mathias/SAE05_mathias
python td/mellier_rendue.py
```

Ce script génère un fichier `resultat_analyse_reseau.csv` avec les paquets analysés.

#### Analyse Avancée avec Détection d'Attaques

```bash
cd /home/runner/work/SAE05_mathias/SAE05_mathias
python testpython/analyse.py
```

Ce script génère :
- `analyse_complet_dns.csv` : analyse complète incluant le trafic DNS
- Rapport de sécurité dans la console

### Personnalisation

Pour analyser vos propres fichiers, modifiez les chemins dans les scripts :

```python
# Dans mellier_rendue.py
input_path = "votre_fichier.txt"
output_path = "votre_sortie.csv"

# Dans analyse.py
fichier_source = "votre_fichier.txt"
```

## 📊 Format des Données

### Entrée (tcpdump)

Les fichiers d'entrée contiennent des captures réseau au format texte tcpdump :

```
12:34:56.789012 IP 192.168.1.10.54321 > 10.0.0.1.80: Flags [S], seq 123456, win 29200, length 0
```

### Sortie (CSV)

Les fichiers CSV générés contiennent les colonnes suivantes :
- Horodatage
- Source_IP (analyse.py uniquement)
- Source_Port
- Dest_IP (analyse.py uniquement)
- Dest_Port
- Flags
- Sequence
- Acknowledgment
- Window
- Length

## 🔒 Détection de Sécurité

Le script `analyse.py` implémente deux types de détection d'attaques :

### Scan de Ports
- **Seuil** : Plus de 10 services/ports différents contactés
- **Indicateur** : Tentative de reconnaissance du réseau

### SYN Flood
- **Seuil** : Plus de 2 paquets SYN depuis une même IP
- **Indicateur** : Tentative de déni de service (DoS)

## 📚 Documentation Associée

Le projet inclut plusieurs documents pédagogiques :
- `SAE-105-.pdf` : Cahier des charges du projet
- `TP2 - SAE1.05.pdf` : Instructions pour les travaux pratiques
- `SAE1.05 - Excel.pdf` et `SAE1.05 - VBA.pdf` : Documentation pour la partie Excel/VBA

## 👨‍💻 Auteur

Mathias - SAE 1.05

## 📝 Notes

- Les fichiers CSV sont ignorés par git (voir `.gitignore`)
- Les données hexadécimales sont automatiquement filtrées lors du parsing
- Le projet supporte les noms d'hôtes et les adresses IP dans les captures
