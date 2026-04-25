
from flask import Flask, request, abort
import subprocess
import multiprocessing
import time

app = Flask(__name__)

def run_process():
    p = subprocess.Popen(['python', '/path/to/file.py'])
    print(f"Process started with PID: {p.pid}")

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
            m = multiprocessing.Process(target=run_process)
            m.start()
            # Optionally: Add logic to track the process if needed.
            return "Logged in! Process started."
        except Exception as e:
            return f"Error! <br> {str(e)}"

    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
