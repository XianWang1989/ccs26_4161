
from flask import Flask, request, abort
import multiprocessing as mp
import subprocess
import sys

app = Flask(__name__)

def run_daemon():
    # Start the subprocess that runs your script
    p = subprocess.Popen(['/path/to/file.py'])
    print("Process created with PID:", p.pid)

@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == "GET":
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
            # Create a new process and start it
            process = mp.Process(target=run_daemon)
            process.start()
            return "Logged in! Daemon process started."
        except Exception as e:
            return "Error! <br> " + str(e)
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
