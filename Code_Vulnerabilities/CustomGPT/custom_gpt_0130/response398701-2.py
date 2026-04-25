
# Store the process globally
daemon_process = None

@app.route("/stop", methods=['POST'])
def stop_process():
    global daemon_process
    if daemon_process is not None:
        daemon_process.terminate()  # Terminate the process
        daemon_process = None  # Clear the reference
        return "Process terminated!"
    return "No process running!"
