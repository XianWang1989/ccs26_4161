
from flask import Flask, request, abort
import subprocess
import threading
import sys

app = Flask(__name__)

def run_daemon():
    # This will start the subprocess in the background
    subprocess.Popen(['python', '/path/to/file.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

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
            # Use threading to run the daemon
            thread = threading.Thread(target=run_daemon)
            thread.daemon = True  # This allows the thread to run independently
            thread.start()  # Start the thread
            return "Logged in!"
        except Exception as e:
            return "Error! <br> " + str(e)
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
