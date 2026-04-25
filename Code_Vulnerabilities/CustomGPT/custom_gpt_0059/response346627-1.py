
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", param1="Hello")

@app.route("/api/param")
def get_param():
    return jsonify(param1="Hello")
