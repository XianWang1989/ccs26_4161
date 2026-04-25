
from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def index():
    # Define parameters to pass
    param1 = "Hello"
    return render_template("index.html", param1=param1)

if __name__ == "__main__":
    app.run(debug=True)
