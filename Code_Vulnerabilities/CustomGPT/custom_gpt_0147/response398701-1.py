
from flask import Flask, request, abort
import subprocess
import threading
import os
import signal

app = Flask(__name__)
process = None

def run_subprocess():
    global process
    process = subprocess.Popen(['/path/to/file.py'])  # Start the subprocess
    process.wait()  # Optionally wait for the process to finish; can be commented out

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
        # Create a thread that runs the subprocess
        threading.Thread(target=run_subprocess, daemon=True).start()
        return "Logged in! Process started!"
    else:
        abort(401)

@app.route("/stop", methods=['POST'])
def stop():
    global process
    if process:
        process.terminate()  # Terminate the subprocess
        process = None  # Clear the reference
        return "Process terminated!"
    else:
        return "No process to terminate."

if __name__ == "__main__":
    app.run(debug=True)
