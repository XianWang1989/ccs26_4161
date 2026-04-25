
from flask import Flask, request, abort
import multiprocessing as mp
import subprocess as sub
import sys
import time

app = Flask(__name__)

def run_process():
    # Start the subprocess as a daemon
    p = sub.Popen(['python', '/path/to/file.py'])
    print("Process created with PID: {}".format(p.pid))

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
            # Create and start the subprocess
            m = mp.Process(target=run_process)
            m.start()
            m.join(0)  # Allow the process to run without waiting for it to finish
            return "Logged in!"
        except Exception as e:
            return "Error! <br> " + str(e)
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
