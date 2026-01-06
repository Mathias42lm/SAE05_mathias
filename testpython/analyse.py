import csv
import os

def extract_val(line, keyword):
    """Extrait une valeur technique (seq, ack, win, length)."""
    if keyword not in line:
        return ""
    try:
        parts = line.split(keyword)
        if len(parts) > 1:
            value = parts[1].strip().split()[0].strip(',').strip(':').strip(']')
            return value
    except:
        pass
    return ""

def separer_ip_port(adresse_complete):
    """
    Sépare l'IP (ou nom d'hôte) du port.
    Ex: '192.168.1.1.80' -> ('192.168.1.1', '80')
    Ex: 'BP-Linux8.ssh' -> ('BP-Linux8', 'ssh')
    """
    if "." not in adresse_complete:
        return adresse_complete, ""
    
    # On coupe au dernier point pour isoler le port
    parts = adresse_complete.rsplit('.', 1)
    return parts[0], parts[1]

def detecter_attaques(data_rows):
    """
    Analyse les métadonnées pour identifier des comportements suspects.
    L'analyse se fait sur l'IP source (sans le port variable).
    """
    stats_ip_source = {}  # { 'IP': set(ports_dest_contactés) }
    stats_syn = {}        # { 'IP': nb_paquets_syn }
    alertes = []

    for row in data_rows:
        ip_src = row["Source_IP"]
        dst_ip = row["Dest_IP"]
        dst_port = row["Dest_Port"]
        flags = row["Flags"]

        # 1. Détection de Scan de Ports
        # On compte combien de ports/destinations différents une IP unique essaie d'atteindre
        if ip_src not in stats_ip_source:
            stats_ip_source[ip_src] = set()
        stats_ip_source[ip_src].add(f"{dst_ip}:{dst_port}")

        # 2. Détection de SYN Flood
        if flags == "S":
            stats_syn[ip_src] = stats_syn.get(ip_src, 0) + 1

    print("\n" + "="*45)
    print("      RAPPORT D'ANALYSE DE SÉCURITÉ (IP)")
    print("="*45)
    
    # Seuil Scan : une IP contacte plus de 10 ports/services différents
    for ip, cibles in stats_ip_source.items():
        if len(cibles) > 10:
            msg = f"[ALERTE] Scan de ports : L'IP {ip} a tenté d'accéder à {len(cibles)} services."
            alertes.append(msg)
            print(msg)

    # Seuil SYN Flood : une IP envoie trop de demandes de connexion
    for ip, nb_syn in stats_syn.items():
        if nb_syn > 2:
            msg = f"[ALERTE] SYN Flood : L'IP {ip} a envoyé {nb_syn} demandes (SYN)."
            alertes.append(msg)
            print(msg)

    if not alertes:
        print("Résultat : Aucun comportement suspect détecté.")
    print("="*45 + "\n")
    return alertes

def parse_tcpdump_flexible(input_path, output_csv, garder_domain=True):
    # En-têtes avec IP et Port séparés
    headers = [
        "Horodatage", "Source_IP", "Source_Port", "Dest_IP", "Dest_Port", 
        "Flags", "Sequence", "Acknowledgment", "Window", "Length"
    ]
    
    data_rows = []

    if not os.path.exists(input_path):
        print(f"Erreur : Le fichier {input_path} n'existe pas.")
        return

    with open(input_path, 'r', encoding='utf-8') as f:
        for line in f:
            if not line.strip() or not line[0].isdigit():
                continue
            
            parts = line.strip().split()
            if len(parts) < 5 or parts[1] != "IP":
                continue

            # --- SÉPARATION IP / PORT ---
            src_ip, src_port = separer_ip_port(parts[2])
            dst_ip, dst_port = separer_ip_port(parts[4].rstrip(':'))

            # Filtre DNS
            if not garder_domain and ("domain" in src_port or "domain" in dst_port):
                continue

            # Extraction technique
            timestamp = parts[0]
            flags = ""
            if "[" in line and "]" in line:
                flags = line[line.find("[")+1 : line.find("]")]
            
            seq = extract_val(line, "seq")
            ack = extract_val(line, "ack")
            win = extract_val(line, "win")
            length = extract_val(line, "length")

            data_rows.append({
                "Horodatage": timestamp, 
                "Source_IP": src_ip, "Source_Port": src_port,
                "Dest_IP": dst_ip, "Dest_Port": dst_port,
                "Flags": flags, "Sequence": seq, "Acknowledgment": ack,
                "Window": win, "Length": length
            })

    # Analyse de sécurité sur les données nettoyées
    detecter_attaques(data_rows)

    # Écriture CSV
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data_rows)
    
    print(f"Fichier CSV créé : {output_csv}")

# --- EXÉCUTION ---
fichier_source = "testpython/fichier1000.txt"

# Génération des deux fichiers (avec et sans DNS)
parse_tcpdump_flexible(fichier_source, "analyse_complet_dns.csv", garder_domain=True)
#parse_tcpdump_flexible(fichier_source, "analyse_donnees_seules.csv", garder_domain=False)