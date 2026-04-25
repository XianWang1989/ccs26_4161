
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    # Pass parameters to the template
    return render_template("index.html", param1="Hello")

if __name__ == "__main__":
    app.run(debug=True)
