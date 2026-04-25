
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    param1 = "Hello"
    return render_template("index.html", param1=param1)

if __name__ == "__main__":
    app.run(debug=True)
