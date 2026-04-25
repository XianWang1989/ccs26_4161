
from flask import Flask, request, abort
from subprocess import Popen
import os

app = Flask(__name__)

def f():
    # This is the subprocess that runs your long-running task
    p = Popen(['python', '/path/to/file.py'])
    print("Process created with PID " + str(p.pid))  # prints to log

@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == "GET":
        # Return an HTML form with a 'Login' button
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
            # Start the long-running process directly
            f()
            return "Logged in!"
        except Exception as e:
            return "Error! <br> " + str(e)
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
