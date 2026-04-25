
from flask import Flask, request, abort
import subprocess
import threading
import time

app = Flask(__name__)

def run_daemon():
    # Starts the subprocess
    p = subprocess.Popen(['/path/to/file.py'])
    print(f"Process created with PID: {p.pid}")  # Log the process ID

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
            # Use a threading.Thread instead of multiprocessing
            thread = threading.Thread(target=run_daemon)
            thread.daemon = True  # Ensure the thread exits when the main program does
            thread.start()
            return "Logged in!"
        except Exception as e:
            return "Error! <br> " + str(e)
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
