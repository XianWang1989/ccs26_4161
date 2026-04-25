
from flask import Flask, request, abort
import multiprocessing as mp
import subprocess as sub
import sys
import time

app = Flask(__name__)

def run_subprocess():
    # Start the subprocess and let it run in the background
    p = sub.Popen(['python', '/path/to/file.py'], stdout=sub.PIPE, stderr=sub.PIPE)
    print("Process created with PID: " + str(p.pid))
    # Optionally, you can handle process output here if needed
    stdout, stderr = p.communicate()  # Capture output (if needed)

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
            # Create and start a new process to run the subprocess function
            m = mp.Process(target=run_subprocess)
            m.start()
            return "Logged in! Process is running in the background."
        except Exception as e:
            return "Error! <br> " + str(e)
    else:
        abort(401)

if __name__ == "__main__":
    app.run()
