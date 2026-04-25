
from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def index():
    data = {
        "param1": "Hello",
        "param2": "World"
    }
    return render_template("index.html", data=json.dumps(data))

if __name__ == "__main__":
    app.run(debug=True)
