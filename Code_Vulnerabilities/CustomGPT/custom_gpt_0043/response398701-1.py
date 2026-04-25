
from flask import Flask, request, abort
import subprocess
import multiprocessing
import time

app = Flask(__name__)

def f():
    """Function to run as a subprocess."""
    p = subprocess.Popen(['/path/to/file.py'])
    print("Process created, PID: " + str(p.pid))

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
            # Start the new process without daemonizing it
            m = multiprocessing.Process(target=f)
            m.start()  # This will not block the Flask server
            # No need for sleep, just start the process
            return "Logged in! Process started."
        except Exception as e:
            return "Error! <br> " + str(e)
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
