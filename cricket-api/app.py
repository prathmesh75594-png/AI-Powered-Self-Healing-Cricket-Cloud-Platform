from flask import Flask, jsonify
from flask_cors import CORS
import time
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)
CORS(app)

START_TIME = time.time()


@app.route("/")
def home():
    return jsonify({
        "service": "Cricket API",
        "status": "running",
        "message": "AI-Powered Self-Healing Cricket Cloud Platform"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "uptime_seconds": round(time.time() - START_TIME, 2)
    })


@app.route("/api/cricket")
def cricket():
    return jsonify({
        "match": "India vs Australia",
        "status": "Live",
        "venue": "Wankhede Stadium",
        "message": "Cricket analytics service is running"
    })


@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)