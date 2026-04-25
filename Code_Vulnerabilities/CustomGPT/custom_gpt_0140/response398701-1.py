
from flask import Flask, request, abort
import subprocess
import os
import signal

app = Flask(__name__)

# Store the process ID globally
process_pid = None

def start_daemon():
    global process_pid
    # Start the subprocess
    process = subprocess.Popen(['python', '/path/to/file.py'])
    process_pid = process.pid
    print(f"Process created with PID: {process_pid}")  # Log process ID

@app.route("/", methods=['POST', 'GET'])
def home():
    global process_pid
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
                <form action="/stop" method="post">
                    <input type="submit" value="Stop Daemon">
                </form>
            </body>
            </html>
        """

    elif request.method == "POST":
        try:
            if process_pid is None or not is_process_running(process_pid):
                start_daemon()
                return "Logged in! Daemon started."
            else:
                return "Daemon is already running!"
        except Exception as e:
            return f"Error! <br> {str(e)}"
    else:
        abort(401)

@app.route("/stop", methods=['POST'])
def stop_daemon():
    global process_pid
    if process_pid and is_process_running(process_pid):
        os.kill(process_pid, signal.SIGTERM)  # Send the kill signal
        process_pid = None
        return "Daemon stopped."
    else:
        return "No daemon process is running."

def is_process_running(pid):
    """Check if a process with the given PID is running."""
    try:
        os.kill(pid, 0)
    except OSError:
        return False
    return True

if __name__ == "__main__":
    app.run(debug=True)
