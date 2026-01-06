import csv
import os

def extract_variable(line, keyword):
    """Cherche un mot-clé (seq, ack, win, length) et extrait la valeur suivante."""
    if keyword not in line:
        return ""
    try:
        # On découpe la ligne juste après le mot-clé
        after_keyword = line.split(keyword)[1].strip()
        # On récupère le premier bloc de texte et on nettoie (virgule, deux-points, etc.)
        value = after_keyword.split()[0].strip(',').strip(':').strip(']')
        return value
    except (IndexError, ValueError):
        return ""

def parse_network_traffic(input_file, output_csv):
    # En-têtes conformes à votre demande
    headers = [
        "Horodatage", "Protocole", "Source_Port", "Destination_Port", 
        "Flags", "Sequence", "Acknowledgment", "Window", "Length"
    ]
    
    parsed_data = []

    if not os.path.exists(input_file):
        print(f"Erreur : Le fichier '{input_file}' est introuvable.")
        return

    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            # RÈGLE ANTI-HEX : On ignore les lignes vides ou celles qui ne commencent pas par un chiffre
            if not line.strip() or not line[0].isdigit():
                continue
            
            parts = line.split()
            # On vérifie que la ligne contient au moins les éléments de base IP
            if len(parts) < 5 or parts[1] != "IP":
                continue

            # 1. Extraction des champs de base
            timestamp = parts[0]
            protocol = parts[1]
            source_and_port = parts[2]
            dest_and_port = parts[4].rstrip(':')
            
            # 2. Extraction des Flags TCP entre crochets [ ]
            flags = ""
            if "[" in line and "]" in line:
                flags = line[line.find("[")+1 : line.find("]")]
            
            # 3. Extraction des variables numériques
            seq = extract_variable(line, "seq")
            ack = extract_variable(line, "ack")
            win = extract_variable(line, "win")
            length = extract_variable(line, "length")

            # On ajoute uniquement si on a bien identifié un paquet
            parsed_data.append({
                "Horodatage": timestamp,
                "Protocole": protocol,
                "Source_Port": source_and_port,
                "Destination_Port": dest_and_port,
                "Flags": flags,
                "Sequence": seq,
                "Acknowledgment": ack,
                "Window": win,
                "Length": length
            })

    # Écriture dans le fichier CSV
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        writer.writerows(parsed_data)
    
    print(f"Succès : {len(parsed_data)} paquets analysés (Hexadécimal ignoré).")
    print(f"Fichier généré : {output_csv}")

# --- Paramètres de fichier ---
input_path = "testpython/fichier182.txt"
output_path = "resultat_analyse_reseau.csv"

# Lancement
parse_network_traffic(input_path, output_path)