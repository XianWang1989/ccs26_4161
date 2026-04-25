
@app.route("/stop", methods=['POST'])
def stop_process():
    # Logic to stop the subprocess
    # You can maintain a reference to the process and terminate it as needed
    return "Process stopped!"
