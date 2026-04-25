
from flask import Flask, request, abort
import subprocess
import threading
import time

app = Flask(__name__)

# This will hold track of the subprocesses
processes = []

def run_process():
    # Replace with the path to your long-running script
    p = subprocess.Popen(['/path/to/file.py'])
    processes.append(p)
    print(f"Process started with PID: {p.pid}")

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
            # Start subprocess in a separate thread
            thread = threading.Thread(target=run_process)
            thread.start()
            return "Logged in! Process running in background."
        except Exception as e:
            return f"Error! <br> {str(e)}"
    else:
        abort(401)

@app.route("/kill", methods=['POST'])
def kill_process():
    if processes:
        p = processes.pop()
        p.terminate()  # or p.kill() for a more forceful termination
        return f"Killed process with PID: {p.pid}"
    return "No process to kill."

if __name__ == "__main__":
    app.run(debug=True)
