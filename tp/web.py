import collections
import datetime
try:
    import install
    if (install.verifier_et_configurer() == 1):
        from flask import Flask, render_template_string, Response
    else:
        import sys
        sys.exit(1)
except ImportError:
    from flask import Flask, render_template_string

app = Flask(__name__)

# Stockage temporaire enrichi
web_storage = {
    "labels": [], "counts": [], 
    "flag_labels": [], "flag_counts": [],
    "alertes": [],
    "evolution_labels": [], "evolution_counts": [], 
    "avg_size": 0, "total_bytes": 0                
}

HTML_DASHBOARD = """
<!DOCTYPE html>
<html>
<head>
    <title>Security Dashboard - Analysis</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body { font-family: 'Segoe UI', sans-serif; margin: 0; background: #1a202c; color: #e2e8f0; }
        .nav { background: #2d3748; color: white; padding: 15px 30px; border-bottom: 2px solid #4a5568; display: flex; justify-content: space-between; align-items: center; }
        .btn-export { background: #3182ce; color: white; border: none; padding: 8px 15px; border-radius: 6px; cursor: pointer; text-decoration: none; font-size: 0.9em; font-weight: bold; transition: 0.3s; }
        .btn-export:hover { background: #2b6cb0; }
        .main { padding: 20px; display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
        .card { background: #2d3748; border-radius: 12px; padding: 20px; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.3); }
        .full-width { grid-column: span 2; }
        h3 { margin-top: 0; color: #edf2f7; border-left: 4px solid #3182ce; padding-left: 10px; font-size: 1.1em; margin-bottom: 20px; }
        .stat-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; text-align: center; }
        .stat-box { background: #1a202c; padding: 15px; border-radius: 8px; border: 1px solid #4a5568; }
        .stat-value { font-size: 1.5em; font-weight: bold; color: #63b3ed; }
        .stat-label { font-size: 0.8em; color: #a0aec0; text-transform: uppercase; }
        table { width: 100%; border-collapse: collapse; }
        th { text-align: left; color: #a0aec0; border-bottom: 1px solid #4a5568; padding: 10px; font-size: 0.85em; }
        td { padding: 10px; border-bottom: 1px solid #4a5568; font-size: 0.85em; }
        .HIGH { color: white; background: #e53e3e; padding: 3px 8px; border-radius: 4px; font-weight: bold; font-size: 0.75em; }
        .MID { color: white; background: #dd6b20; padding: 3px 8px; border-radius: 4px; font-weight: bold; font-size: 0.75em; }
        .chart-container { position: relative; height: 250px; width: 100%; }
    </style>
</head>
<body>
    <div class="nav">
        <h1>DASHBOARD DE SÉCURITÉ</h1>
        <a href="/export" class="btn-export">📥 Exporter Rapport (.md)</a>
    </div>
    
    <div class="main">
        <div class="card full-width">
            <h3>📈 Évolution du Trafic (Paquets / Temps)</h3>
            <div class="chart-container"><canvas id="lineChart"></canvas></div>
        </div>

        <div class="card">
            <h3>📊 Volume & Tailles</h3>
            <div class="stat-grid">
                <div class="stat-box">
                    <div class="stat-value">{{avg_size}}</div>
                    <div class="stat-label">Taille Moyenne (Octets)</div>
                </div>
                <div class="stat-box">
                    <div class="stat-value">{{total_bytes // 1024}}</div>
                    <div class="stat-label">Total Transféré (KB)</div>
                </div>
            </div>
        </div>

        <div class="card">
            <h3>🥧 Distribution Globale (Camembert)</h3>
            <div class="chart-container"><canvas id="pieChart"></canvas></div>
        </div>

        <div class="card">
            <h3>Analyse des Flags TCP</h3>
            <div class="chart-container"><canvas id="radarChart"></canvas></div>
        </div>

        <div class="card">
            <h3>Top 10 IP (Volume)</h3>
            <div class="chart-container"><canvas id="barChart"></canvas></div>
        </div>

        <div class="card full-width">
            <h3>Alertes Comportementales</h3>
            <table>
                <thead><tr><th>IP Source</th><th>Type</th><th>Détails</th><th>Gravité</th></tr></thead>
                <tbody>
                    {% for a in alertes %}
                    <tr><td>{{a.ip}}</td><td>{{a.type}}</td><td>{{a.details}}</td><td><span class="{{a.niveau}}">{{a.niveau}}</span></td></tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
    </div>

    <script>
        const colors = ['#3182ce', '#38a169', '#e53e3e', '#d69e2e', '#805ad5', '#319795', '#718096', '#f6e05e', '#f687b3', '#4a5568'];

        // Line Chart (Evolution)
        new Chart(document.getElementById('lineChart'), {
            type: 'line',
            data: {
                labels: {{ evolution_labels|tojson }},
                datasets: [{ 
                    label: 'Paquets', 
                    data: {{ evolution_counts|tojson }}, 
                    borderColor: '#63b3ed', 
                    backgroundColor: 'rgba(99, 179, 237, 0.1)',
                    fill: true,
                    tension: 0.3 
                }]
            },
            options: { responsive: true, maintainAspectRatio: false }
        });

        // Pie Chart (Camembert)
        new Chart(document.getElementById('pieChart'), {
            type: 'pie',
            data: {
                labels: {{ labels|tojson }},
                datasets: [{
                    data: {{ counts|tojson }},
                    backgroundColor: colors,
                    borderColor: '#2d3748',
                    borderWidth: 2
                }]
            },
            options: { responsive: true, maintainAspectRatio: false, plugins: { legend: { position: 'bottom', labels: { color: '#a0aec0' } } } }
        });

        // Bar Chart
        new Chart(document.getElementById('barChart'), {
            type: 'bar',
            data: {
                labels: {{ labels|tojson }},
                datasets: [{ label: 'Paquets', data: {{ counts|tojson }}, backgroundColor: '#3182ce' }]
            },
            options: { responsive: true, maintainAspectRatio: false }
        });

        // Radar Chart
        new Chart(document.getElementById('radarChart'), {
            type: 'radar',
            data: {
                labels: {{ flag_labels|tojson }},
                datasets: [{
                    label: 'Flags',
                    data: {{ flag_counts|tojson }},
                    backgroundColor: 'rgba(49, 130, 206, 0.2)',
                    borderColor: '#3182ce'
                }]
            },
            options: { responsive: true, maintainAspectRatio: false }
        });
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_DASHBOARD, **web_storage)

@app.route('/export')
def export_md():
    total_paquets = sum(web_storage["counts"])
    nb_alertes = len(web_storage["alertes"])
    alertes_critiques = len([a for a in web_storage["alertes"] if a['niveau'] == "HIGH"])
    
    md = "# 🛡️ Rapport Complet d'Analyse et de Sécurité Réseau\n\n"
    
    # 1. RÉSUMÉ EXÉCUTIF
    md += "## 📝 Résumé Exécutif\n"
    md += "| Indicateur | Valeur |\n"
    md += "| :--- | :--- |\n"
    md += f"| 📦 Volume Total | {total_paquets} paquets |\n"
    md += f"| ⚖️ Taille Moyenne | {web_storage['avg_size']} octets |\n"
    md += f"| 📂 Données Totales | {web_storage['total_bytes'] / 1024:.2f} KB |\n"
    md += f"| 🔥 Alertes Critiques | {alertes_critiques} |\n"
    md += f"| 🕒 Statut Global | {'🔴 CRITIQUE' if alertes_critiques > 0 else '🟢 SAIN'} |\n\n"

    # 2. ÉVOLUTION TEMPORELLE (Evolution des paquets par rapport au temps)
    md += "## 📈 Évolution du Trafic Temporel\n"
    md += "Ce tableau montre la charge réseau par seconde enregistrée.\n\n"
    md += "| Horodatage | Nombre de Paquets |\n"
    md += "| :--- | :--- |\n"
    for t, c in zip(web_storage["evolution_labels"], web_storage["evolution_counts"]):
        md += f"| {t} | {c} |\n"
    md += "\n"

    # 3. DISTRIBUTION GLOBALE (Représentation du camembert)
    md += "## 🥧 Distribution Globale des Sources\n"
    md += "| Adresse IP | Volume | Part du Trafic |\n"
    md += "| :--- | :--- | :--- |\n"
    for ip, count in zip(web_storage["labels"], web_storage["counts"]):
        part = (count / total_paquets * 100) if total_paquets > 0 else 0
        md += f"| `{ip}` | {count} | {part:.1f}% |\n"

    # 4. ALERTES
    md += "\n## ⚠️ Alertes de Sécurité\n"
    if nb_alertes == 0:
        md += "✅ Aucune menace détectée.\n"
    else:
        md += "| Gravité | IP Source | Type | Détails |\n"
        md += "| :--- | :--- | :--- | :--- |\n"
        for a in web_storage["alertes"]:
            md += f"| {a['niveau']} | `{a['ip']}` | {a['type']} | {a['details']} |\n"

    return Response(md, mimetype="text/markdown", headers={"Content-disposition": "attachment; filename=rapport_securite.md"})

def start_server(rows, alerts):
    # 1. Top 10 IP
    counts = collections.Counter([r.get("Source_IP") for r in rows])
    top_10 = counts.most_common(10)
    web_storage["labels"] = [x[0] for x in top_10]
    web_storage["counts"] = [x[1] for x in top_10]
    
    # 2. Flags TCP
    flag_list = []
    for r in rows:
        f = r.get("Flags", "")
        if f: flag_list.extend([x.strip() for x in f.split(',')])
    flag_data = collections.Counter(flag_list)
    web_storage["flag_labels"] = list(flag_data.keys())
    web_storage["flag_counts"] = list(flag_data.values())

    # 3. Évolution Temporelle
    time_data = collections.Counter([r.get("Horodatage", "").split('.')[0] for r in rows])
    sorted_times = sorted(time_data.items())
    web_storage["evolution_labels"] = [x[0] for x in sorted_times]
    web_storage["evolution_counts"] = [x[1] for x in sorted_times]

    # 4. Taille Moyenne des Paquets
    sizes = [int(r["Length"]) for r in rows if r.get("Length") and r["Length"].isdigit()]
    web_storage["total_bytes"] = sum(sizes)
    web_storage["avg_size"] = round(sum(sizes) / len(sizes), 2) if sizes else 0

    web_storage["alertes"] = alerts
    app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)