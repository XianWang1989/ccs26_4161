
from flask import Flask, request, abort
import threading
import subprocess
import sys
import time

app = Flask(__name__)

def run_subprocess():
    # Start your subprocess here
    p = subprocess.Popen(['python', '/path/to/file.py'])
    print("Process created with PID:", p.pid)

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
            # Create and start a thread
            thread = threading.Thread(target=run_subprocess)
            thread.daemon = True  # Enable daemon mode
            thread.start()
            time.sleep(1)  # Optional wait for the process to start
            return "Logged in!"
        except Exception as e:
            return "Error! <br> " + str(e)
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
