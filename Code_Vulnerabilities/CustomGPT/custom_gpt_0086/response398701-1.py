
from flask import Flask, request, abort
import subprocess
import threading
import os

app = Flask(__name__)

def run_daemon():
    # Replace '/path/to/file.py' with your actual script path
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
            thread = threading.Thread(target=run_daemon)
            thread.daemon = True  # Daemonize the thread
            thread.start()        # Start the thread
            return "Logged in!"
        except Exception as e:
            return f"Error! <br> {str(e)}"
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
