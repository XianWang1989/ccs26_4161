
from flask import Flask, request, abort
import subprocess
import os
import signal

app = Flask(__name__)

def run_daemon():
    # This creates a new session and detaches the subprocess
    subprocess.Popen(['/path/to/file.py'], preexec_fn=os.setsid)  # Use `os.setsid()` to detach in Unix-like systems

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
            # Spawn a separate process to run your daemon
            run_daemon()
            return "Logged in and process started!"
        except Exception as e:
            return "Error! <br> " + str(e)
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
