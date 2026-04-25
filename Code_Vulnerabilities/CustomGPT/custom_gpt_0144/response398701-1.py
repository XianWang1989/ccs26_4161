from flask import Flask, request, abort
import subprocess
import os

app = Flask(__name__)

# Global variable to store process handle
process_handle = None

@app.route("/", methods=['GET', 'POST'])
def home():
    global process_handle
    if request.method == "GET":
        return """
        <!DOCTYPE html>
        <html>
          <body>
            <h2>Daemon Trigger</h2>
            <form method="post">
              <input type="submit" name="action" value="Start Daemon">
              <input type="submit" name="action" value="Stop Daemon">
            </form>
          </body>
        </html>
        """

    elif request.method == "POST":
        action = request.form.get("action")
        if action == "Start Daemon":
            if process_handle is None or process_handle.poll() is not None:
                process_handle = subprocess.Popen(
                    ['python3', '/path/to/file.py'],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                    start_new_session=True  # prevents it from being killed when Flask ends
                )
                return f"Started daemon process with PID: {process_handle.pid}"
            else:
                return "Daemon is already running."
        elif action == "Stop Daemon":
            if process_handle and process_handle.poll() is None:
                process_handle.terminate()
                process_handle.wait()
                return "Daemon process terminated."
            else:
                return "No running daemon process."
        else:
            return "Unknown action."
    else:
        abort(401)
