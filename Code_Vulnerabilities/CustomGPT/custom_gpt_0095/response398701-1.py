
from flask import Flask, request, abort
import subprocess
import multiprocessing
import time

app = Flask(__name__)

def run_daemon():
    # Start the subprocess
    p = subprocess.Popen(['python3', '/path/to/file.py'])
    print(f"Subprocess started with PID: {p.pid}")  # Log the PID

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
            # Create and start a new process
            m = multiprocessing.Process(target=run_daemon)
            m.start()
            return "Logged in! The daemon process has been started."

        except Exception as e:
            return f"Error! <br> {str(e)}"
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
