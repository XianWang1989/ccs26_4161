
from flask import Flask, request, abort
import subprocess
import multiprocessing
import time

app = Flask(__name__)

def run_daemon():
    # Starts the subprocess
    p = subprocess.Popen(['python', '/path/to/script.py'])
    print("Process created with PID: {}".format(p.pid))

@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == "GET":
        # Return an HTML form with a 'Login' button
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
            # Create and start the daemon process
            m = multiprocessing.Process(target=run_daemon)
            m.start()

            # Return response immediately
            return "Logged in! Process running in background."

        except Exception as e:
            return "Error! <br> {}".format(str(e))
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
