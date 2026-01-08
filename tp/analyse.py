import csv
import os

def extract_val(line, keyword):
    """Cherche un mot-clé (seq, ack, win, length) et extrait la valeur suivante."""
    if keyword not in line:
        return ""
    try:
        parts = line.split(keyword)
        if len(parts) > 1:
            # Nettoie les caractères comme , : ou ] collés à la valeur
            value = parts[1].strip().split()[0].strip(',').strip(':').strip(']')
            return value
    except:
        pass
    return ""

def separer_ip_port(adresse_complete):
    """Sépare l'IP du port. '192.168.1.1.80' -> ('192.168.1.1', '80')"""
    if "." not in adresse_complete:
        return adresse_complete, ""
    parts = adresse_complete.rsplit('.', 1)
    return parts[0], parts[1]

def detecter_attaques(data_rows):
    """Analyse comportementale sur l'IP source (sans le port source)."""
    stats_ip_source = {}
    stats_syn = {}
    alertes_web = []

    for row in data_rows:
        ip_src = row["Source_IP"]
        dst_full = f"{row['Dest_IP']}:{row['Dest_Port']}"
        flags = row["Flags"]

        # 1. Détection de Scan (Nombre de ports différents visés par une seule IP)
        if ip_src not in stats_ip_source:
            stats_ip_source[ip_src] = set()
        stats_ip_source[ip_src].add(dst_full)

        # 2. Détection de SYN Flood (Paquets de demande de connexion [S])
        if flags == "S":
            stats_syn[ip_src] = stats_syn.get(ip_src, 0) + 1

    # Création du rapport pour le Web
    for ip, cibles in stats_ip_source.items():
        if len(cibles) > 10:
            alertes_web.append({
                "type": "Scan de Ports", "ip": ip,
                "details": f"Tentative sur {len(cibles)} services.", "niveau": "MID"
            })

    for ip, nb_syn in stats_syn.items():
        if nb_syn > 50:
            alertes_web.append({
                "type": "SYN Flood", "ip": ip,
                "details": f"Envoi de {nb_syn} paquets SYN.", "niveau": "HIGH"
            })

    return alertes_web

def parse_tcpdump_flexible(input_path, output_csv, garder_domain=True):
    headers = ["Horodatage", "Source_IP", "Source_Port", "Dest_IP", "Dest_Port", 
               "Flags", "Sequence", "Acknowledgment", "Window", "Length"]
    data_rows = []

    if not os.path.exists(input_path):
        return [], []

    with open(input_path, 'r', encoding='utf-8') as f:
        for line in f:
            # Anti-Hex : On ignore les lignes qui ne commencent pas par un chiffre
            if not line.strip() or not line[0].isdigit():
                continue
            
            parts = line.strip().split()
            if len(parts) < 5 or parts[1] != "IP":
                continue

            src_ip, src_port = separer_ip_port(parts[2])
            dst_ip, dst_port = separer_ip_port(parts[4].rstrip(':'))

            # Filtre DNS (recherche port 53 ou nom 'domain')
            est_dns = src_port in ["domain", "53"] or dst_port in ["domain", "53"]
            if not garder_domain and est_dns:
                continue

            flags = ""
            if "[" in line and "]" in line:
                flags = line[line.find("[")+1 : line.find("]")]
            
            data_rows.append({
                "Horodatage": parts[0], "Source_IP": src_ip, "Source_Port": src_port,
                "Dest_IP": dst_ip, "Dest_Port": dst_port, "Flags": flags,
                "Sequence": extract_val(line, "seq"), "Acknowledgment": extract_val(line, "ack"),
                "Window": extract_val(line, "win"), "Length": extract_val(line, "length")
            })

    # Analyse de sécurité
    alertes = detecter_attaques(data_rows)

    # Sauvegarde CSV physique
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data_rows)
    
    return data_rows, alertes