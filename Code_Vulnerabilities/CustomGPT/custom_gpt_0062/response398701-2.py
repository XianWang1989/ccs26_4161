
@app.route("/stop", methods=['POST'])
def stop_process():
    pid = request.form.get('pid')
    if pid:
        try:
            os.kill(int(pid), 9)  # Use SIGKILL to terminate the process
            return "Process with PID {} stopped.".format(pid)
        except Exception as e:
            return "Error stopping process: {}".format(str(e))
    return "No PID provided."
