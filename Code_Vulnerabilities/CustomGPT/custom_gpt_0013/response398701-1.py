
from flask import Flask, request, abort
import subprocess
import multiprocessing as mp
import os
import time

app = Flask(__name__)

def run_subprocess():
    # Start the subprocess
    process = subprocess.Popen(['python', '/path/to/file.py'])
    print(f"Process created with PID: {process.pid}")
    process.wait()  # Wait for the process to finish (if required)

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
            m = mp.Process(target=run_subprocess)
            m.start()
            return "Logged in! Process started with PID: {}".format(m.pid)
        except Exception as e:
            return "Error! <br> " + str(e)
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
