
from flask import Flask, request, abort
import multiprocessing as mp
import subprocess
import sys

app = Flask(__name__)

def run_subprocess():
    """Function to run the subprocess."""
    p = subprocess.Popen(['python', '/path/to/file.py'])  # Use 'python' for cross-platform compatibility
    print("Process created with PID: " + str(p.pid))  # Logs the process ID

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
            # Start the subprocess in a new process
            m = mp.Process(target=run_subprocess)
            m.start()  # Start the process
            # No need for a sleep; the process runs independently
            return "Logged in and process started!"
        except Exception as e:
            return "Error! <br> " + str(e)
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
