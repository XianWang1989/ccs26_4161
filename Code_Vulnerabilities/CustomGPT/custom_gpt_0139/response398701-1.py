
from flask import Flask, request, abort
from multiprocessing import Process
import subprocess
import time

app = Flask(__name__)

def run_daemon():
    # This is where the subprocess will be executed.
    p = subprocess.Popen(['python3', '/path/to/file.py'])  # adjust the command as needed
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
            # Create and start a new Process
            m = Process(target=run_daemon)
            m.start()

            # No need to wait here; we simply return the response
            return "Logged in! Process is running!"

        except Exception as e:
            return f"Error! <br> {str(e)}"
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
