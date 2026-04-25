
from flask import Flask, request, abort
import subprocess
import multiprocessing as mp
import os
import signal

app = Flask(__name__)

def start_process():
    # Starting the subprocess to run the script. Adjust the path if needed.
    p = subprocess.Popen(['python', '/path/to/file.py'], preexec_fn=os.setsid)
    print("Process created: PID =", p.pid)

    # Wait for the process to finish if needed, else do other work.
    p.wait()

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
            # Start the process in a separate process
            m = mp.Process(target=start_process)
            m.start()
            return "Logged in! Process started."
        except Exception as e:
            return "Error!<br>" + str(e)
    else:
        abort(401)

# Endpoint to kill the process
@app.route("/kill", methods=['POST'])
def kill_process():
    # You will need to manage process IDs via some mechanism (like a global variable or database)
    # For simplicity, assume we save the last started PID
    global last_pid
    if last_pid:
        os.killpg(last_pid, signal.SIGTERM)  # Send the term signal to the process group
        return "Process killed."
    return "No process to kill."

if __name__ == "__main__":
    last_pid = None  # Store last process ID
    app.run(debug=True)
