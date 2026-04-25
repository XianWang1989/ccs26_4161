
from flask import Flask, request, abort
import subprocess
import threading
import time

app = Flask(__name__)

def start_process():
    # Launch the subprocess without waiting for it to finish
    p = subprocess.Popen(['python', '/path/to/file.py'])
    print("Process created with PID:", p.pid)

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
            # Start a new thread to handle the process
            thread = threading.Thread(target=start_process)
            thread.daemon = True  # This allows the program to exit even if the thread is still running
            thread.start()
            return "Logged in! Process started."
        except Exception as e:
            return "Error! <br> " + str(e)
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
