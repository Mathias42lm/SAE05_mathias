import collections
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

# Stockage temporaire
web_storage = {
    "labels": [], "counts": [], 
    "flag_labels": [], "flag_counts": [],
    "alertes": []
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
        .status { font-size: 0.8em; color: #68d391; background: rgba(104, 211, 145, 0.1); padding: 5px 12px; border-radius: 20px; }
        .btn-export { background: #3182ce; color: white; border: none; padding: 8px 15px; border-radius: 6px; cursor: pointer; text-decoration: none; font-size: 0.9em; font-weight: bold; transition: 0.3s; }
        .btn-export:hover { background: #2b6cb0; }
        .main { 
            padding: 20px; 
            display: grid; 
            grid-template-columns: 1fr 1fr; 
            gap: 20px; 
        }
        
        .card { background: #2d3748; border-radius: 12px; padding: 20px; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.3); }
        .full-width { grid-column: span 2; }
        
        h3 { margin-top: 0; color: #edf2f7; border-left: 4px solid #3182ce; padding-left: 10px; font-size: 1.1em; margin-bottom: 20px; }
        table { width: 100%; border-collapse: collapse; }
        th { text-align: left; color: #a0aec0; border-bottom: 1px solid #4a5568; padding: 10px; font-size: 0.85em; }
        td { padding: 10px; border-bottom: 1px solid #4a5568; font-size: 0.85em; }
        
        .nb-packets { font-family: monospace; color: #63b3ed; font-weight: bold; }
        .HIGH { color: white; background: #e53e3e; padding: 3px 8px; border-radius: 4px; font-weight: bold; font-size: 0.75em; }
        .MID { color: white; background: #dd6b20; padding: 3px 8px; border-radius: 4px; font-weight: bold; font-size: 0.75em; }
        
        .chart-container { position: relative; height: 300px; width: 100%; }
    </style>
</head>
<body>
    <div class="nav">
        <h1>DASHBOARD DE SÉCURITÉ</h1>
        <a href="/export" class="btn-export">📥 Exporter Rapport (.md)</a>
    </div>
    
    <div class="main">
        <div class="card">
            <h3>Top 10 IP (Volume par paquets)</h3>
            <div class="chart-container"><canvas id="barChart"></canvas></div>
        </div>

        <div class="card">
            <h3>Analyse des Flags TCP</h3>
            <div class="chart-container"><canvas id="radarChart"></canvas></div>
        </div>

        <div class="card">
            <h3>Distribution Globale</h3>
            <div class="chart-container"><canvas id="pieChart"></canvas></div>
        </div>

        <div class="card">
            <h3>Alertes Comportementales</h3>
            <table>
                <thead>
                    <tr><th>IP Source</th><th>Type</th><th>Paquets</th><th>Gravité</th></tr>
                </thead>
                <tbody>
                    {% for a in alertes %}
                    <tr>
                        <td>{{a.ip}}</td><td>{{a.type}}</td>
                        <td class="nb-packets">{{a.nb_packets}}</td>
                        <td><span class="{{a.niveau}}">{{a.niveau}}</span></td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
    </div>

    <script>
        const colors = ['#3182ce', '#38a169', '#e53e3e', '#d69e2e', '#805ad5', '#319795', '#718096', '#f6e05e', '#f687b3', '#4a5568'];

        // Bar Chart
        new Chart(document.getElementById('barChart'), {
            type: 'bar',
            data: {
                labels: {{ labels|tojson }},
                datasets: [{ label: 'Paquets', data: {{ counts|tojson }}, backgroundColor: '#3182ce', borderRadius: 4 }]
            },
            options: { responsive: true, maintainAspectRatio: false, plugins: { legend: { display: false } } }
        });

        // Radar Chart (TCP Flags)
        new Chart(document.getElementById('radarChart'), {
            type: 'radar',
            data: {
                labels: {{ flag_labels|tojson }},
                datasets: [{
                    label: 'Flags détectés',
                    data: {{ flag_counts|tojson }},
                    backgroundColor: 'rgba(49, 130, 206, 0.2)',
                    borderColor: '#3182ce',
                    pointBackgroundColor: '#3182ce'
                }]
            },
            options: { 
                responsive: true, maintainAspectRatio: false,
                scales: { r: { grid: { color: '#4a5568' }, pointLabels: { color: '#a0aec0' }, ticks: { display: false } } }
            }
        });

        // Pie Chart (Camembert) avec Légende
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
            options: {
                responsive: true, maintainAspectRatio: false,
                plugins: {
                    legend: { 
                        display: true, 
                        position: 'bottom',
                        labels: { color: '#a0aec0', boxWidth: 12, padding: 20 }
                    }
                }
            }
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
    """Génère un fichier Markdown basé sur les données actuelles."""
    md = "# 🛡️ Rapport d'Analyse Réseau\n\n"
    
    md += "## 📊 Top 10 IP par Volume\n"
    md += "| Adresse IP | Nombre de Paquets |\n"
    md += "| :--- | :--- |\n"
    for ip, count in zip(web_storage["labels"], web_storage["counts"]):
        md += f"| {ip} | {count} |\n"
    
    md += "\n## 🚩 Analyse des Flags TCP\n"
    for flag, count in zip(web_storage["flag_labels"], web_storage["flag_counts"]):
        md += f"* **{flag}**: {count} paquets\n"
    
    md += "\n## ⚠️ Alertes de Sécurité\n"
    md += "| IP Source | Type d'Alerte | Gravité |\n"
    md += "| :--- | :--- | :--- |\n"
    for a in web_storage["alertes"]:
        md += f"| {a['ip']} | {a['type']} | {a['niveau']} |\n"
    
    return Response(
        md,
        mimetype="text/markdown",
        headers={"Content-disposition": "attachment; filename=rapport_securite.md"}
    )

def start_server(rows, alerts):
    """
    Traitement des données et démarrage du serveur Flask.
    """
    # Analyse Top 10 IP
    counts = collections.Counter([r.get("Source_IP") for r in rows])
    top_10 = counts.most_common(10)
    web_storage["labels"] = [x[0] for x in top_10]
    web_storage["counts"] = [x[1] for x in top_10]
    
    # Analyse des Flags TCP
    flag_list = []
    for r in rows:
        f = r.get("Flags", "")
        if f: flag_list.extend([x.strip() for x in f.split(',')])
    
    flag_data = collections.Counter(flag_list)
    web_storage["flag_labels"] = list(flag_data.keys())
    web_storage["flag_counts"] = list(flag_data.values())

    # Alertes
    web_storage["alertes"] = alerts
    
    app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)