
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    data = {"param1": "Hello"}
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
