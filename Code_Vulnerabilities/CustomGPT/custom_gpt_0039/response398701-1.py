
from flask import Flask, request, abort
import subprocess
import multiprocessing
import time

app = Flask(__name__)

def run_subprocess():
    """Function to run the subprocess."""
    p = subprocess.Popen(['python', '/path/to/file.py'])  # Update with the correct path
    print("Process created with PID: {}".format(p.pid))

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
            process = multiprocessing.Process(target=run_subprocess)
            process.start()
            return "Logged in and process started!", 200
        except Exception as e:
            return "Error! <br> {}".format(str(e)), 500
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
