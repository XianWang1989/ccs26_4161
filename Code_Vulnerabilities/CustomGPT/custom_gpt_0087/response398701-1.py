
from flask import Flask, request, abort
import subprocess
import multiprocessing as mp
import sys

app = Flask(__name__)

def run_daemon():
    # Start the subprocess and return immediately
    subprocess.Popen(['python', '/path/to/file.py'], close_fds=True)

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
            # Start the daemon process
            daemon_process = mp.Process(target=run_daemon)
            daemon_process.start()
            return "Logged in!"
        except Exception as e:
            return f"Error! <br> {str(e)}"
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
