from flask import Flask
import socket
import os
import time

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "application": "Self Healing Demo",
        "hostname": socket.gethostname(),
        "status": "Healthy"
    }

@app.route("/health")
def health():
    if os.path.exists("/tmp/unhealthy"):
        return "Unhealthy", 500
    return "OK", 200

@app.route("/fail")
def fail():
    open("/tmp/unhealthy", "w").close()
    return "Failure injected", 200

@app.route("/recover")
def recover():
    if os.path.exists("/tmp/unhealthy"):
        os.remove("/tmp/unhealthy")
    return "Failure cleared", 200

@app.route("/cpu")
def cpu():
    x = 0
    while True:
        x += 1

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
