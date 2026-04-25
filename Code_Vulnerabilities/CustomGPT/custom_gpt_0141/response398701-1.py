
from flask import Flask, request, abort
import subprocess
import threading
import os
import time

app = Flask(__name__)

def start_daemon():
    # Start the subprocess, replace with your actual subprocess command
    p = subprocess.Popen(['python', '/path/to/file.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(f"Daemon process started with PID: {p.pid}")

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
            # Use threading to start the daemon without blocking the main Flask thread
            thread = threading.Thread(target=start_daemon)
            thread.daemon = True  # Ensure the thread exists only with the main program
            thread.start()
            time.sleep(1)  # Optional: Wait a moment to ensure daemon starts

            return "Logged in! Daemon process is running."
        except Exception as e:
            return f"Error! <br> {str(e)}"
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
