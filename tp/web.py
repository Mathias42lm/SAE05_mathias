import install
if (install.verifier_et_configurer() == 1):
    from flask import Flask, render_template_string
    import collections
else:
    import sys
    sys.exit(1)

app = Flask(__name__)

# Stockage temporaire des données analysées
web_storage = {"labels": [], "counts": [], "alertes": []}

HTML_DASHBOARD = """
<!DOCTYPE html>
<html>
<head>
    <title>Network Analyzer Dashboard</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body { font-family: 'Segoe UI', sans-serif; margin: 0; background: #f4f7f9; }
        .nav { background: #2c3e50; color: white; padding: 15px 30px; }
        .main { padding: 30px; display: grid; grid-template-columns: 1fr 1fr; gap: 30px; }
        .card { background: white; border-radius: 8px; padding: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); }
        table { width: 100%; border-collapse: collapse; }
        th, td { padding: 12px; text-align: left; border-bottom: 1px solid #eee; }
        .Rouge { color: white; background: #e74c3c; padding: 4px 8px; border-radius: 4px; }
        .Orange { color: white; background: #f39c12; padding: 4px 8px; border-radius: 4px; }
    </style>
</head>
<body>
    <div class="nav"><h1>DASHBOARD DE SÉCURITÉ</h1></div>
    <div class="main">
        <div class="card">
            <h3>Top 10 - Activité par IP</h3>
            <canvas id="chart"></canvas>
        </div>
        <div class="card">
            <h3>Alertes Comportementales</h3>
            <table>
                <tr><th>IP Source</th><th>Type</th><th>Gravité</th></tr>
                {% for a in alertes %}
                <tr><td>{{a.ip}}</td><td>{{a.type}}</td><td><span class="{{a.niveau}}">{{a.niveau}}</span></td></tr>
                {% endfor %}
            </table>
        </div>
    </div>
    <script>
        new Chart(document.getElementById('chart'), {
            type: 'bar',
            data: {
                labels: {{ labels|tojson }},
                datasets: [{ label: 'Paquets', data: {{ counts|tojson }}, backgroundColor: '#3498db' }]
            }
        });
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_DASHBOARD, 
                                  labels=web_storage["labels"], 
                                  counts=web_storage["counts"], 
                                  alertes=web_storage["alertes"])

def start_server(rows, alerts):
    # Préparer les données pour Chart.js (Top 10 IPs)
    counts = collections.Counter([r["Source_IP"] for r in rows])
    top_10 = counts.most_common(10)
    
    web_storage["labels"] = [x[0] for x in top_10]
    web_storage["counts"] = [x[1] for x in top_10]
    web_storage["alertes"] = alerts
    
    # Lancement du serveur (pas de debug/reloader car lancé via thread)
    app.run(port=5000, debug=False, use_reloader=False)