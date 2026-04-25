
from flask import Flask, request, abort
import subprocess
import os

app = Flask(__name__)

def run_daemon_process():
    # Start the subprocess as a background process
    subprocess.Popen(['python', '/path/to/file.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

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
            run_daemon_process()  # Call the function to run the subprocess
            return "Logged in!"
        except Exception as e:
            return f"Error! <br> {str(e)}"

    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
