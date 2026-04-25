
from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/params")
def params():
    return jsonify(param1="Hello")

if __name__ == '__main__':
    app.run(debug=True)
