
@app.route("/stop", methods=['POST'])
def stop_daemon():
    # Replace with your logic to find the daemon process and stop it
    pid = ...  # Get the PID of the running process you want to stop
    try:
        os.killpid, signal.SIGTERM)  # Use SIGTERM to gracefully terminate
        return "Process stopped!"
    except Exception as e:
        return "Error stopping process: " + str(e)
