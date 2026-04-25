
from flask import Flask, request, abort
import subprocess
import threading
import sys

app = Flask(__name__)

def run_daemon():
    # Start the subprocess
    p = subprocess.Popen(['/path/to/file.py'])
    print("Daemon process started with PID:", p.pid)

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
            # Create and start a thread to run the daemon
            daemon_thread = threading.Thread(target=run_daemon)
            daemon_thread.daemon = True  # Make thread a daemon
            daemon_thread.start()
            return "Logged in! Daemon process will run in the background."
        except Exception as e:
            return "Error! <br> " + str(e)
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
