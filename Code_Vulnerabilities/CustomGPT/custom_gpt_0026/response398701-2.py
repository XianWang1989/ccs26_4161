
import os
import signal

@app.route("/stop", methods=['POST'])
def stop():
    # Here you need to track the PID of the subprocess if you want to kill it
    # For example, you can store the PID in a variable when starting and call:
    os.kill(pid, signal.SIGTERM)  # Replace 'pid' with the actual PID
    return "Daemon stopped."
