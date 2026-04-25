
from flask import Flask, request, abort
import subprocess
import threading
import time

app = Flask(__name__)

def run_subprocess():
    # Replace with the path to your script
    subprocess.Popen(['python', '/path/to/file.py'])

@app.route("/", methods=['GET', 'POST'])
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
            # Start thread to run subprocess
            thread = threading.Thread(target=run_subprocess)
            thread.daemon = True
            thread.start()
            return "Logged in! Process started."
        except Exception as e:
            return "Error! <br> " + str(e)
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
