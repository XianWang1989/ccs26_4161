
@app.route("/stop", methods=['POST'])
def stop():
    try:
        # Find the process ID of the subprocess and terminate it
        os.system("pkill -f /path/to/file.py")  # Adjust based on how you track the PID
        return "Process stopped!"
    except Exception as e:
        return "Error stopping process: " + str(e)
