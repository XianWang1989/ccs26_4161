
process = None  # To store the process reference

@app.route("/start", methods=['POST'])
def start():
    global process
    process = mp.Process(target=start_process)
    process.start()
    return "Process started!"

@app.route("/stop", methods=['POST'])
def stop():
    global process
    if process is not None:
        process.terminate()  # Terminate the process
        process.join()  # Wait for the process to end
        return "Process stopped!"
    else:
        return "No process to stop!"
