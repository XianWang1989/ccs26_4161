
from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def index():
    params = {"param1": "Hello"}
    return render_template("index.html", params=json.dumps(params))

if __name__ == "__main__":
    app.run(debug=True)
