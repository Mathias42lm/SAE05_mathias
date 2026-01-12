import csv
import os

def extract_val(line, keyword):
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
    """Sépare l'IP du port de manière plus robuste."""
    # tcpdump utilise souvent IP.Port (ex: 192.168.1.1.80)
    # On vérifie s'il y a au moins un point
    if "." not in adresse_complete:
        return adresse_complete, ""
    
    parts = adresse_complete.rsplit('.', 1)
    
    # On vérifie si la dernière partie est un port (chiffres) ou un service connu
    if parts[1].isdigit() or parts[1] in ["http", "https", "domain", "ssh", "ftp"]:
        return parts[0], parts[1]
    
    # Si ce n'est pas un port, toute la chaîne est l'IP/Hostname
    return adresse_complete, ""

def detecter_attaques(data_rows):
    """Analyse les comportements et compte les paquets incriminés."""
    scans_ports = {}    # { src_ip: set(ports_visés) }
    packet_count_scan = {} # { src_ip: nb_total_paquets_scan }
    syn_counts = {}     # { src_ip: count }
    ssh_attempts = {}  # Détection du brute force SSH
    alertes_web = []

    # --- SEUILS ---
    LIMIT_SYN_HIGH = 50
    LIMIT_SYN_MID = LIMIT_SYN_HIGH / 2
    LIMIT_SCAN_PORTS = 10 
    LIMIT_SCAN_MAX = LIMIT_SCAN_PORTS + 30
    LIMIT_SSH_ATTEMPTS = 15 # Seuil pour les tentatives SSH

    for row in data_rows:
        ip_src = row["Source_IP"]
        port_dst = row["Dest_Port"]
        flags = row["Flags"]

        # 1. LOGIQUE SCAN DE PORTS
        if ip_src not in scans_ports:
            scans_ports[ip_src] = set()
            packet_count_scan[ip_src] = 0
        
        if port_dst:
            scans_ports[ip_src].add(port_dst)
            packet_count_scan[ip_src] += 1 # On compte chaque paquet envoyé vers un port

        # 2. LOGIQUE SYN FLOOD
        if flags == "S":
            syn_counts[ip_src] = syn_counts.get(ip_src, 0) + 1
        # 3. LOGIQUE BRUTE FORCE SSH
        if port_dst in ["22", "ssh"]:
            ssh_attempts[ip_src] = ssh_attempts.get(ip_src, 0) + 1

    # --- GÉNÉRATION DES ALERTES AVEC NOMBRE DE PAQUETS ---

    # Analyse SYN Flood
    for ip, count in ssh_attempts.items():
        if count >= LIMIT_SSH_ATTEMPTS:
            alertes_web.append({
                "ip": ip, "type": "Brute Force SSH", 
                "details": f"Tentatives excessives sur port 22 ({count} paquets)", 
                "niveau": "HIGH"
            })
    for ip, count in syn_counts.items():
        if count >= LIMIT_SYN_MID:
            niveau = "HIGH" if count >= LIMIT_SYN_HIGH else "MID"
            alertes_web.append({
                "ip": ip, 
                "type": "SYN Flood", 
                "nb_packets": count, # Nombre de paquets SYN détectés
                "details": f"Attaque par inondation ({count} paquets SYN)", 
                "niveau": niveau
            })

    # Analyse Scan de Ports
    for ip, ports in scans_ports.items():
        if len(ports) > LIMIT_SCAN_PORTS:
            total_pkts = packet_count_scan[ip]
            niveau = "HIGH" if count >= LIMIT_SCAN_MAX else "MID"
            alertes_web.append({
                "ip": ip, 
                "type": "Scan de Ports", 
                "nb_packets": total_pkts, # Nombre total de paquets durant le scan
                "details": f"Scan sur {len(ports)} ports ({total_pkts} paquets)", 
                "niveau": niveau
            })

    return alertes_web

def parse_tcpdump_flexible(input_path, output_csv, garder_domain=True):
    headers = ["Horodatage", "Source_IP", "Source_Port", "Dest_IP", "Dest_Port", 
               "Flags", "Sequence", "Acknowledgment", "Window", "Length"]
    data_rows = []

    if not os.path.exists(input_path):
        print(f"Erreur : {input_path} introuvable.")
        return [], []

    with open(input_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or not line[0].isdigit(): continue
            
            parts = line.split()
            if len(parts) < 5 or parts[1] != "IP": continue

            # Nettoyage des adresses (enlève le ':' final si présent)
            src_raw = parts[2]
            dst_raw = parts[4].rstrip(':')

            src_ip, src_port = separer_ip_port(src_raw)
            dst_ip, dst_port = separer_ip_port(dst_raw)

            if not garder_domain:
                if src_port in ["53", "domain"] or dst_port in ["53", "domain"]:
                    continue

            # Extraction des Flags [S], [S.], [P.], etc.
            flags = ""
            if "[" in line and "]" in line:
                flags = line[line.find("[")+1 : line.find("]")]
            
            data_rows.append({
                "Horodatage": parts[0], "Source_IP": src_ip, "Source_Port": src_port,
                "Dest_IP": dst_ip, "Dest_Port": dst_port, "Flags": flags,
                "Sequence": extract_val(line, "seq"), "Acknowledgment": extract_val(line, "ack"),
                "Window": extract_val(line, "win"), "Length": extract_val(line, "length")
            })

    alertes = detecter_attaques(data_rows)

    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data_rows)
    return data_rows, alertes