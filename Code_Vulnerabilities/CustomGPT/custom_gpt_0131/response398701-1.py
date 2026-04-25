
from flask import Flask, request, abort
import subprocess
import threading
import time

app = Flask(__name__)

def run_subprocess():
    # Replace '/path/to/file.py' with the actual path
    subprocess.Popen(['python', '/path/to/file.py'])
    print("Subprocess started.")

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
            # Start subprocess in a separate thread
            threading.Thread(target=run_subprocess).start()
            return "Logged in!"
        except Exception as e:
            return f"Error! <br> {str(e)}"
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
