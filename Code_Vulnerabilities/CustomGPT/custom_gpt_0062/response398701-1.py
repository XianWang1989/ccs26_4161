
from flask import Flask, request, abort
import subprocess
import os
import sys
import multiprocessing as mp

app = Flask(__name__)

def run_subprocess():
    # Call your long-running script here
    subprocess.Popen(['python', '/path/to/file.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == "GET":
        # Return an HTML form with a 'Login' button
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
            # Start a new process to run the long-running script
            process = mp.Process(target=run_subprocess)
            process.start()
            return "Logged in! Process started with PID: {}".format(process.pid)
        except Exception as e:
            return "Error! <br> {}".format(str(e))
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
