
from flask import Flask, request, abort
import subprocess
import os
import signal

app = Flask(__name__)

def run_daemon():
    # Start your long-running process here
    subprocess.Popen(['python', '/path/to/your_script.py'], 
                     preexec_fn=os.setpgrp)  # Start in a new process group

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
            run_daemon()  # Start the daemon process without blocking
            return "Logged in! Daemon process started."
        except Exception as e:
            return f"Error! <br> {str(e)}"
    else:
        abort(401)

@app.route("/kill", methods=['POST'])
def kill_daemon():
    # Implement logic to kill the daemon if required
    os.killpg(os.getpgid(process.pid), signal.SIGTERM)  # Replace with actual PID management
    return "Daemon process terminated."

if __name__ == "__main__":
    app.run(debug=True)
