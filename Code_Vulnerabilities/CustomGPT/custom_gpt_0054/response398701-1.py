
from flask import Flask, request, abort
import subprocess
import os

app = Flask(__name__)

def run_subprocess():
    # Start your long-running subprocess here
    subprocess.Popen(['python', '/path/to/file.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == "GET":
        # Return an HTML form with a 'Login' button
        return """
        <!DOCTYPE html>
        <html>
            <head></head>
            <body>
                Testing Login
                <form action="/" method="post">
                    <input type="submit" value="Login">
                </form>
            </body>
        </html>
        """

    elif request.method == "POST":
        try:
            run_subprocess()
            return "Logged in and process started!"
        except Exception as e:
            return "Error! <br> " + str(e)
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
