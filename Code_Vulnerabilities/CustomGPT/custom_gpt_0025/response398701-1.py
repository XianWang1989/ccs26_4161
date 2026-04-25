
from flask import Flask, request, abort
import subprocess
import threading
import sys

app = Flask(__name__)

def run_subprocess():
    # Start the long-running subprocess
    p = subprocess.Popen(['/path/to/file.py'])
    print(f"Process created: {p.pid}")  # prints the PID to log

@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == "GET":
        return """
        <!DOCTYPE html>
        <html>
            <head></head>
            <body>
                Testing Login
                <form action="/" method="POST">
                    <input type="submit" value="Login">
                </form>
            </body>
        </html>
        """
    elif request.method == "POST":
        try:
            # Start a new thread for the subprocess
            thread = threading.Thread(target=run_subprocess)
            thread.daemon = True  # Set the thread as a daemon
            thread.start()  # Start the thread

            return "Logged in! The process is running in the background."
        except Exception as e:
            return f"Error! <br> {str(e)}"
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
