
from flask import Flask, request, abort
import subprocess
import threading

app = Flask(__name__)

# Global variable to keep track of process
process = None

def run_process():
    global process
    process = subprocess.Popen(['python', '/path/to/file.py'])  # Adjust script path
    process.wait()  # Keep process running until it completes

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
              <input type="submit" value="Start Daemon">
            </form>
            <form action="/stop" method="post">
              <input type="submit" value="Stop Daemon">
            </form>
          </body>
        </html>
        """

    elif request.method == "POST":
        if 'Start Daemon' in request.form:
            if process is None or process.poll() is not None:  # None or finished
                threading.Thread(target=run_process, daemon=True).start()
                return "Daemon started!"
            else:
                return "Daemon is already running!"
        else:
            return abort(400)  # Invalid action

@app.route("/stop", methods=['POST'])
def stop():
    global process
    if process and process.poll() is None:  # Check if running
        process.terminate()
        process = None
        return "Daemon stopped!"
    else:
        return "No running daemon to stop!"

if __name__ == "__main__":
    app.run(debug=True)
