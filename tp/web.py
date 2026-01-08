import install
if (install.verifier_et_configurer() == 1):
    from flask import Flask, render_template_string
    import collections
else:
    import sys
    sys.exit(1)

app = Flask(__name__)

# Stockage temporaire enrichi pour inclure le nombre de paquets
web_storage = {"labels": [], "counts": [], "alertes": []}

HTML_DASHBOARD = """
<!DOCTYPE html>
<html>
<head>
    <title>Network Analyzer Dashboard</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body { font-family: 'Segoe UI', sans-serif; margin: 0; background: #1a202c; color: #e2e8f0; }
        .nav { background: #2d3748; color: white; padding: 15px 30px; border-bottom: 2px solid #4a5568; }
        .main { padding: 30px; display: grid; grid-template-columns: 1.2fr 0.8fr; gap: 30px; }
        .card { background: #2d3748; border-radius: 12px; padding: 25px; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.3); }
        h3 { margin-top: 0; color: #edf2f7; border-left: 4px solid #3182ce; padding-left: 10px; }
        table { width: 100%; border-collapse: collapse; margin-top: 15px; }
        th { text-align: left; color: #a0aec0; border-bottom: 1px solid #4a5568; padding: 12px; font-size: 0.9em; }
        td { padding: 12px; border-bottom: 1px solid #4a5568; font-size: 0.85em; }
        .nb-packets { font-family: monospace; color: #63b3ed; font-weight: bold; }
        .HIGH { color: white; background: #e53e3e; padding: 4px 10px; border-radius: 4px; font-weight: bold; font-size: 0.8em; }
        .MID { color: white; background: #dd6b20; padding: 4px 10px; border-radius: 4px; font-weight: bold; font-size: 0.8em; }
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
                <thead>
                    <tr>
                        <th>IP Source</th>
                        <th>Type</th>
                        <th>Nb Paquets</th>
                        <th>Gravité</th>
                    </tr>
                </thead>
                <tbody>
                    {% for a in alertes %}
                    <tr>
                        <td>{{a.ip}}</td>
                        <td>{{a.type}}</td>
                        <td class="nb-packets">{{a.nb_packets}}</td>
                        <td><span class="{{a.niveau}}">{{a.niveau}}</span></td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
    </div>
    <script>
        new Chart(document.getElementById('chart'), {
            type: 'bar',
            data: {
                labels: {{ labels|tojson }},
                datasets: [{ 
                    label: 'Total Paquets vus', 
                    data: {{ counts|tojson }}, 
                    backgroundColor: '#3182ce',
                    borderRadius: 5
                }]
            },
            options: {
                plugins: { legend: { labels: { color: '#a0aec0' } } },
                scales: {
                    y: { grid: { color: '#4a5568' }, ticks: { color: '#a0aec0' } },
                    x: { grid: { display: false }, ticks: { color: '#a0aec0' } }
                }
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
    """
    Met à jour les données et lance le serveur Flask.
    alerts doit être une liste de dict contenant 'nb_packets'.
    """
    counts = collections.Counter([r["Source_IP"] for r in rows])
    top_10 = counts.most_common(10)
    
    web_storage["labels"] = [x[0] for x in top_10]
    web_storage["counts"] = [x[1] for x in top_10]
    web_storage["alertes"] = alerts
    
    # Lancement du serveur sur le port 5000
    app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)