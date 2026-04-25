
from flask import Flask, request, abort
import subprocess
import os
import signal
import time

app = Flask(__name__)

# This will store the PIDs of running daemons
running_processes = {}

def start_process():
    # Start the subprocess and store its PID
    p = subprocess.Popen(['python', '/path/to/file.py'])  # Ensure the path to your script is correct
    print(f"Process created: {p.pid}")  # Log the PID
    return p.pid

def stop_process(pid):
    # Kill the subprocess if it's running
    try:
        os.kill(pid, signal.SIGTERM)
        print(f"Process {pid} terminated.")
    except OSError:
        print(f"Process {pid} not found.")

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
            # Start a subprocess
            pid = start_process()
            running_processes[pid] = True  # Store the PID in the dictionary for later reference
            return "Logged in!"
        except Exception as e:
            return f"Error! <br> {str(e)}"

    else:
        abort(401)

@app.route("/stop", methods=['POST'])
def stop():
    if request.method == "POST":
        try:
            # Here you may want to stop a running process using a specific PID
            if running_processes:
                pid = next(iter(running_processes))  # Get the first running process PID
                stop_process(pid)  # Stop the process
                del running_processes[pid]  # Remove from running processes
                return f"Stopped process {pid}."
            else:
                return "No running processes to stop."
        except Exception as e:
            return f"Error! <br> {str(e)}"

    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
