from flask import Flask
import socket
import os
import time

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "application":"Self Healing Demo",
        "hostname":socket.gethostname(),
        "status":"Healthy"
    }

@app.route("/health")
def health():
    return "OK",200

@app.route("/cpu")
def cpu():
    x=0
    while True:
        x+=1

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)
