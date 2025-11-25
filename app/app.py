from flask import Flask, render_template_string, jsonify
import os
from datetime import datetime
import socket

app = Flask(__name__)

# Variables de entorno de GitLab CI para Creacion de Imagen
BUILD_VERSION = os.getenv('CI_COMMIT_SHORT_SHA', 'dev')
COMMIT_SHA = os.getenv('CI_COMMIT_SHA', 'local')
PIPELINE_ID = os.getenv('CI_PIPELINE_ID', 'N/A')
PIPELINE_URL = os.getenv('CI_PIPELINE_URL', '#')
JOB_ID = os.getenv('CI_JOB_ID', 'N/A')
COMMIT_MESSAGE = os.getenv('CI_COMMIT_MESSAGE', 'Local development')
COMMIT_AUTHOR = os.getenv('CI_COMMIT_AUTHOR', 'Developer')
DEPLOYED_AT = datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
HOSTNAME = socket.gethostname()


HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pipeline - DevSecOps - Complete</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        
        .container {
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            max-width: 800px;
            width: 100%;
            padding: 40px;
            animation: fadeIn 0.5s ease-in;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .header {
            text-align: center;
            margin-bottom: 40px;
            padding-bottom: 20px;
            border-bottom: 3px solid #667eea;
        }
        
        .header h1 {
            color: #667eea;
            font-size: 2.5em;
            margin-bottom: 10px;
        }
        
        .header .subtitle {
            color: #666;
            font-size: 1.2em;
        }
        
        .status-badge {
            display: inline-block;
            background: #10b981;
            color: white;
            padding: 8px 20px;
            border-radius: 20px;
            font-weight: bold;
            margin-top: 10px;
            animation: pulse 2s infinite;
        }
        
        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.05); }
        }
        
        .info-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }
        
        .info-card {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
        }
        
        .info-card:hover {
            transform: translateY(-5px);
        }
        
        .info-card .label {
            color: #667eea;
            font-weight: bold;
            font-size: 0.9em;
            text-transform: uppercase;
            margin-bottom: 5px;
        }
        
        .info-card .value {
            color: #333;
            font-size: 1.2em;
            font-weight: 600;
            word-break: break-all;
        }
        
        .commit-info {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            border-left: 4px solid #667eea;
            margin-bottom: 20px;
        }
        
        .commit-info .message {
            color: #333;
            font-style: italic;
            margin-bottom: 10px;
        }
        
        .commit-info .author {
            color: #666;
            font-size: 0.9em;
        }
        
        .footer {
            text-align: center;
            color: #999;
            font-size: 0.9em;
            margin-top: 30px;
            padding-top: 20px;
            border-top: 1px solid #ddd;
        }
        
        .links {
            display: flex;
            gap: 10px;
            justify-content: center;
            margin-top: 20px;
        }
        
        .btn {
            display: inline-block;
            padding: 12px 24px;
            background: #667eea;
            color: white;
            text-decoration: none;
            border-radius: 8px;
            font-weight: bold;
            transition: all 0.3s ease;
        }
        
        .btn:hover {
            background: #5568d3;
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
        }
        
        .btn-secondary {
            background: #10b981;
        }
        
        .btn-secondary:hover {
            background: #059669;
        }
        
        @media (max-width: 600px) {
            .container {
                padding: 20px;
            }
            
            .header h1 {
                font-size: 1.8em;
            }
            
            .info-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🚀 Python App Main</h1>
            <p class="subtitle">DevSecOps Pipeline</p>
            <span class="status-badge">✓ Running</span>
        </div>
        
        <div class="commit-info">
            <div class="label">💬 Last Commit:</div>
            <div class="message">{{ commit_message }}</div>
            <div class="author">👤 by {{ commit_author }}</div>
        </div>
        
        <div class="info-grid">
            <div class="info-card">
                <div class="label">📦 Build Version</div>
                <div class="value">{{ build_version }}</div>
            </div>
            
            <div class="info-card">
                <div class="label">🔨 Pipeline ID</div>
                <div class="value">{{ pipeline_id }}</div>
            </div>
            
            <div class="info-card">
                <div class="label">🔑 Commit SHA</div>
                <div class="value">{{ commit_sha[:12] }}...</div>
            </div>
            
            <div class="info-card">
                <div class="label">⏰ Deployed At</div>
                <div class="value">{{ deployed_at }}</div>
            </div>
            
            <div class="info-card">
                <div class="label">🖥️ Hostname</div>
                <div class="value">{{ hostname }}</div>
            </div>
            
            <div class="info-card">
                <div class="label">💼 Job ID</div>
                <div class="value">{{ job_id }}</div>
            </div>
        </div>
        
        <div class="links">
            <a href="/health" class="btn btn-secondary">Health Check</a>
            <a href="/info" class="btn">API Info</a>
            {% if pipeline_url != '#' %}
            <a href="{{ pipeline_url }}" class="btn" target="_blank">View Pipeline</a>
            {% endif %}
        </div>
        
        <div class="footer">
            <p>🛡️ Built with DevSecOps Best Practices</p>
            <p>GitLab CI/CD + k3s + Docker + DefectDojo</p>
        </div>
    </div>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(
        HTML_TEMPLATE,
        build_version=BUILD_VERSION,
        commit_sha=COMMIT_SHA,
        pipeline_id=PIPELINE_ID,
        pipeline_url=PIPELINE_URL,
        job_id=JOB_ID,
        commit_message=COMMIT_MESSAGE,
        commit_author=COMMIT_AUTHOR,
        deployed_at=DEPLOYED_AT,
        hostname=HOSTNAME
    )

@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'build_version': BUILD_VERSION,
        'hostname': HOSTNAME
    }), 200

@app.route('/info')
def info():
    return jsonify({
        'application': 'Python Flask DevSecOps Demo',
        'version': BUILD_VERSION,
        'commit_sha': COMMIT_SHA,
        'pipeline_id': PIPELINE_ID,
        'job_id': JOB_ID,
        'commit_message': COMMIT_MESSAGE,
        'commit_author': COMMIT_AUTHOR,
        'deployed_at': DEPLOYED_AT,
        'hostname': HOSTNAME,
        'environment': os.getenv('FLASK_ENV', 'production')
    }), 200

if __name__ == '__main__':
    # Test 
    host = os.getenv("FLASK_RUN_HOST", "127.0.0.1")  
    port = int(os.getenv("FLASK_RUN_PORT", "5000"))

    app.run(host=host, port=port, debug=False)