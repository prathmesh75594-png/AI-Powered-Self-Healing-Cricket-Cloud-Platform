from flask import Flask, jsonify
from flask_cors import CORS
import time

app = Flask(__name__)
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)