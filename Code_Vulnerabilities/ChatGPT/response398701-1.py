
from flask import Flask, request, abort
import multiprocessing
import time
import os
import signal

app = Flask(__name__)

def long_running_process():
    """Function to simulate a long-running subprocess."""
    print(f"Starting process with PID: {os.getpid()}")
    while True:
        time.sleep(10)  # Simulate doing some work
        print("Process is still running...")

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
        # Start a long-running process in a separate non-daemon process
        process = multiprocessing.Process(target=long_running_process)
        process.start()
        return f"Logged in! Process started with PID: {process.pid}"
    else:
        abort(401)

@app.route("/stop", methods=['POST'])
def stop_process():
    # Logic to stop the process could go here
    # We would need a mechanism to track the running processes, for this mockup we skip it.
    return "Stop process endpoint is not implemented."

if __name__ == "__main__":
    app.run(debug=True)
