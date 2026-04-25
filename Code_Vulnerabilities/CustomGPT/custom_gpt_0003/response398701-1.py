
from flask import Flask, request, abort
import multiprocessing as mp
import subprocess as sub
import time

app = Flask(__name__)

def run_daemon():
    # This function will be triggered to run the daemonized process
    p = sub.Popen(['python', '/path/to/file.py'])  # Ensure correct Python interpreter
    print("Daemon process created with PID:", p.pid)

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
            # Create a new process that runs the daemon code
            m = mp.Process(target=run_daemon)
            m.start()  # Start the process but do not join, so it'll run independently
            return "Logged in!"
        except Exception as e:
            return "Error! <br> " + str(e)
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
