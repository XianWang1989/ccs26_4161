
from flask import Flask, request, abort
import subprocess
import multiprocessing
import time
import os

app = Flask(__name__)

def run_daemon():
    # Start the subprocess
    p = subprocess.Popen(['python', '/path/to/file.py'])  # Ensure your file is executable
    print(f"Process created with PID: {p.pid}")

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
            # Start the daemon process
            m = multiprocessing.Process(target=run_daemon)
            m.start()
            return "Logged in!"
        except Exception as e:
            return f"Error!<br>{str(e)}"
    else:
        abort(401)

if __name__ == "__main__":
    app.run(threaded=True)  # Run Flask with threading
