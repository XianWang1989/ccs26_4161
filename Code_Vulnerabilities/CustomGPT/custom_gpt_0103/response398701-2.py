
running_process = None

def run_subprocess():
    global running_process
    running_process = subprocess.Popen(['python', '/path/to/file.py'])
    print("Process created with PID:", running_process.pid)

@app.route("/stop", methods=['POST'])
def stop_process():
    global running_process
    if running_process:
        running_process.terminate()  # Send terminate signal
        running_process = None
        return "Process terminated!"
    return "No process to terminate."
