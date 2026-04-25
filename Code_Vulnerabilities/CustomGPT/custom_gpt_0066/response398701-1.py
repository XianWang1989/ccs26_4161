
from flask import Flask, request, abort
import subprocess
import os
import atexit

app = Flask(__name__)

# Store process IDs for later termination
processes = []

def cleanup():
    for pid in processes:
        try:
            os.kill(pid, 0)  # Check if process is still running
        except ProcessLookupError:
            continue  # Process already terminated

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
            # Start subprocess
            p = subprocess.Popen(['python', '/path/to/file.py'])
            processes.append(p.pid)  # Keep track of process ID
            atexit.register(cleanup)  # Ensure cleanup on exit
            return "Logged in! Process ID: {}".format(p.pid)
        except Exception as e:
            return "Error occurred: {}".format(e)
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
