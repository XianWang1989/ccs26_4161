
from flask import Flask, request, abort
import subprocess
import threading
import time
import os

app = Flask(__name__)

# Use a global variable to keep track of the process
process = None

def start_process():
    global process
    process = subprocess.Popen(['/path/to/file.py'])  # Adjust the path as necessary
    print("Process created:", process.pid)

@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == "GET":
        # Return an HTML form with a 'Login' button
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
              <form action="/stop" method="post">
                <input type="submit" value="Stop Process">
              </form>
            </body>
          </html>
          """

    elif request.method == "POST":
        # Start the process
        if process is None:  # Check if there is already a running process
            thread = threading.Thread(target=start_process)
            thread.start()
            time.sleep(1)  # Wait for the process to be created (optional)
            return "Logged in! Process started."
        else:
            return "Process is already running!"

    else:
        abort(401)

@app.route("/stop", methods=['POST'])
def stop_process():
    global process
    if process is not None:
        os.kill(process.pid, subprocess.signal.SIGTERM)  # Graceful termination
        process = None
        return "Process stopped."
    else:
        return "No process is currently running."

if __name__ == "__main__":
    app.run(debug=True)
