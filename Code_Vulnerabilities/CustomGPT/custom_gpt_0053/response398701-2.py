
process_pid = None

@app.route("/stop", methods=["POST"])
def stop_process():
    global process_pid
    if process_pid:
        try:
            subprocess.Popen(["kill", str(process_pid)])
            process_pid = None
            return "Process terminated."
        except Exception as e:
            return f"Error! <br> {str(e)}"
    else:
        return "No process to stop."
