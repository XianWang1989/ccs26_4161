
from flask import Flask, request, abort
import subprocess
import threading
import time

app = Flask(__name__)

def run_daemon():
    # Start the daemon subprocess
    process = subprocess.Popen(['python', '/path/to/file.py'])
    print(f"Process created: {process.pid}")

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
        # Start the daemon in a separate thread
        thread = threading.Thread(target=run_daemon)
        thread.daemon = True  # Set as daemon thread
        thread.start()  # Start the thread

        return "Logged in!"

    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
