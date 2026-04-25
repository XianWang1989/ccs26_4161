
from flask import Flask, request, abort
import subprocess
import multiprocessing
import time

app = Flask(__name__)

def long_running_process():
    # Replace this with your actual long-running task
    subprocess.Popen(['/path/to/file.py'])
    print("Process started.")

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
            # Start a new process for the long-running task
            m = multiprocessing.Process(target=long_running_process)
            m.start()  # Start the process
            return "Logged in and process started!"
        except Exception as e:
            return f"Error! <br> {str(e)}"

    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
