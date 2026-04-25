
from flask import Flask, request, abort
import subprocess
import sys

app = Flask(__name__)

def run_subprocess():
    # Start the long-running process
    subprocess.Popen(['/path/to/file.py'])  # Replace with your actual script path
    print("Process started.")

@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == "GET":
        return """
        <!DOCTYPE html>
        <html>
            <head>
            </head>
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
            run_subprocess()  # Start the subprocess directly
            return "Logged in! Process is running in the background."
        except Exception as e:
            return "Error! <br> " + str(e)
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
