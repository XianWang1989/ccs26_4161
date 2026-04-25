
active_process = None

def run_daemon():
    global active_process
    active_process = subprocess.Popen(['/path/to/file.py'])

@app.route("/stop", methods=['POST'])
def stop_daemon():
    global active_process
    if active_process is not None:
        active_process.terminate()  # Stop the process
        active_process = None
        return "Daemon stopped."
    return "No active daemon to stop."
