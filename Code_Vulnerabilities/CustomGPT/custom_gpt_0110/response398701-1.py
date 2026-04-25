
from flask import Flask, request, abort
import subprocess
import multiprocessing
import sys

app = Flask(__name__)

def run_subprocess():
    # Run the subprocess without blocking
    subprocess.Popen(['python', '/path/to/file.py'])

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
            # Start the subprocess in a separate process
            m = multiprocessing.Process(target=run_subprocess)
            m.start()  # This won't block
            return "Logged in!"
        except Exception as e:
            return "error! <br> " + str(e)
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
