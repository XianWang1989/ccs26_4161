
import os

# global variable to store the Popen object
proc = None

def run_subprocess():
    global proc
    proc = subprocess.Popen(['python', '/path/to/file.py'])

@app.route("/stop", methods=['POST'])
def stop_process():
    global proc
    if proc:
        proc.terminate()  # Gracefully terminate the process
        return "Process stopped."
    else:
        return "No process to stop."
