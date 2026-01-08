import collections
try:
    import install
    if (install.verifier_et_configurer() == 1):
        from flask import Flask, render_template_string
    else:
        import sys
        sys.exit(1)
except ImportError:
    from flask import Flask, render_template_string

app = Flask(__name__)

# Stockage temporaire
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
        
        /* Grille à 3 colonnes pour accueillir le camembert */
        .main { 
            padding: 20px; 
            display: grid; 
            grid-template-columns: 1fr 1fr 1.2fr; 
            gap: 20px; 
        }
        
        .card { background: #2d3748; border-radius: 12px; padding: 20px; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.3); }
        h3 { margin-top: 0; color: #edf2f7; border-left: 4px solid #3182ce; padding-left: 10px; font-size: 1.1em; }
        
        table { width: 100%; border-collapse: collapse; margin-top: 15px; }
        th { text-align: left; color: #a0aec0; border-bottom: 1px solid #4a5568; padding: 10px; font-size: 0.85em; }
        td { padding: 10px; border-bottom: 1px solid #4a5568; font-size: 0.8em; }
        
        .nb-packets { font-family: monospace; color: #63b3ed; font-weight: bold; }
        .HIGH { color: white; background: #e53e3e; padding: 3px 8px; border-radius: 4px; font-weight: bold; font-size: 0.75em; }
        .MID { color: white; background: #dd6b20; padding: 3px 8px; border-radius: 4px; font-weight: bold; font-size: 0.75em; }
        
        .chart-container { position: relative; height: 300px; width: 100%; }
    </style>
</head>
<body>
    <div class="nav"><h1>DASHBOARD DE SÉCURITÉ</h1></div>
    <div class="main">
        <div class="card">
            <h3>Volume par IP (Barres)</h3>
            <div class="chart-container">
                <canvas id="barChart"></canvas>
            </div>
        </div>

        <div class="card">
            <h3>Distribution du Trafic (Top 10)</h3>
            <div class="chart-container">
                <canvas id="pieChart"></canvas>
            </div>
        </div>

        <div class="card">
            <h3>Alertes Comportementales</h3>
            <table>
                <thead>
                    <tr>
                        <th>IP Source</th>
                        <th>Type</th>
                        <th>Paquets</th>
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
        const labels = {{ labels|tojson }};
        const counts = {{ counts|tojson }};
        const colors = [
            '#3182ce', '#38a169', '#e53e3e', '#d69e2e', '#805ad5', 
            '#319795', '#718096', '#f6e05e', '#f687b3', '#4a5568'
        ];

        // Configuration de l'Histogramme
        new Chart(document.getElementById('barChart'), {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{ label: 'Paquets', data: counts, backgroundColor: '#3182ce', borderRadius: 4 }]
            },
            options: {
                responsive: true, maintainAspectRatio: false,
                plugins: { legend: { display: false } },
                scales: {
                    y: { grid: { color: '#4a5568' }, ticks: { color: '#a0aec0' } },
                    x: { ticks: { display: false } }
                }
            }
        });

        // Configuration du Camembert (Pie Chart)
        new Chart(document.getElementById('pieChart'), {
            type: 'pie',
            data: {
                labels: labels,
                datasets: [{
                    data: counts,
                    backgroundColor: colors,
                    borderColor: '#2d3748',
                    borderWidth: 2
                }]
            },
            options: {
                responsive: true, maintainAspectRatio: false,
                plugins: {
                    legend: { 
                        position: 'bottom',
                        labels: { color: '#a0aec0', boxWidth: 10, font: { size: 10 } }
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
    return render_template_string(HTML_DASHBOARD, 
                                  labels=web_storage["labels"], 
                                  counts=web_storage["counts"], 
                                  alertes=web_storage["alertes"])

def start_server(rows, alerts):
    """
    Met à jour les données et lance le serveur Flask.
    """
    counts = collections.Counter([r["Source_IP"] for r in rows])
    top_10 = counts.most_common(10)
    
    web_storage["labels"] = [x[0] for x in top_10]
    web_storage["counts"] = [x[1] for x in top_10]
    web_storage["alertes"] = alerts
    
    app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)