
from flask import Flask, request, abort
import subprocess
import threading

app = Flask(__name__)

def run_subprocess():
    p = subprocess.Popen(['python', '/path/to/file.py'])  # Adjust the path to your script
    print("Process created with PID:", p.pid)  # Print to log

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
            # Start the subprocess in a separate thread
            thread = threading.Thread(target=run_subprocess)
            thread.start()
            return "Logged in! Process is running."
        except Exception as e:
            return "Error: " + str(e)
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
