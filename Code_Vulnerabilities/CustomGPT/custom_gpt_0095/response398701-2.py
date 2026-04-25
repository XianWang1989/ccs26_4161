
processes = {}

@app.route("/stop", methods=['POST'])
def stop_process():
    pid = request.form.get("pid")
    if pid and pid.isdigit() and int(pid) in processes:
        subprocess.call(['kill', pid])
        del processes[int(pid)]
        return "Process stopped."
    abort(400)

# Update the home function to save the PID
elif request.method == "POST":
    try:
        m = multiprocessing.Process(target=run_daemon)
        m.start()
        processes[m.pid] = m  # Store the process reference
        return f"Logged in! The daemon process has been started with PID: {m.pid}."
