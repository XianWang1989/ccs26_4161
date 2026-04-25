
from flask import Flask, request, abort
import subprocess
import os
import signal

app = Flask(__name__)

# This will hold the process ID of the subprocess
daemon_process = None

def start_daemon():
    global daemon_process
    # Start the subprocess that runs in the background
    daemon_process = subprocess.Popen(['python3', '/path/to/file.py'])

@app.route("/", methods=['POST', 'GET'])
def home():
    global daemon_process
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
            # Start the daemon
            start_daemon()
            return "Logged in! Daemon PID: {}".format(daemon_process.pid)
        except Exception as e:
            return "Error! <br> " + str(e)
    else:
        abort(401)

@app.route("/stop", methods=['POST'])
def stop_daemon():
    global daemon_process
    if daemon_process:
        os.kill(daemon_process.pid, signal.SIGTERM)  # Terminate the process
        return "Daemon stopped."
    else:
        return "No daemon is running."

if __name__ == "__main__":
    app.run(debug=True)
