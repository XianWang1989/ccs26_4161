
from flask import Flask, request, abort
import subprocess
import threading
import os
import sys

app = Flask(__name__)

def start_daemon_process():
    # Start the subprocess in the background
    p = subprocess.Popen(['python', '/path/to/file.py'])
    print(f"Process created with PID: {p.pid}")  # Log the PID

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
            # Use a thread to run the daemon process
            thread = threading.Thread(target=start_daemon_process)
            thread.daemon = True
            thread.start()
            return "Logged in!"
        except Exception as e:
            return f"Error! <br> {str(e)}"
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
