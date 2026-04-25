
from flask import Flask, request, abort
import subprocess
import concurrent.futures
import os

app = Flask(__name__)

# A thread pool executor for managing subprocesses
executor = concurrent.futures.ThreadPoolExecutor(max_workers=5)

def run_subprocess():
    """Function to run the subprocess."""
    p = subprocess.Popen(['python', '/path/to/your/script.py'])
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
            # Submit the subprocess to the executor
            executor.submit(run_subprocess)
            return "Logged in! The process is running in the background."
        except Exception as e:
            return "Error! <br>" + str(e)
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
