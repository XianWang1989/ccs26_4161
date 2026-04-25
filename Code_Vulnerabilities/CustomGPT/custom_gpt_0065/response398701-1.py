
from flask import Flask, request, abort
import subprocess
import threading

app = Flask(__name__)

def start_process():
    """Function to start the subprocess."""
    p = subprocess.Popen(['/path/to/file.py'])  # Change to your actual script path
    print("Process created with PID:", p.pid)

@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == "GET":
        return """
        <!DOCTYPE html>
        <html>
            <head></head>
            <body>
                Testing Login
                <form action="/" method="post">
                    <input type="submit" value="Login">
                </form>
            </body>
        </html>
        """

    elif request.method == "POST":
        try:
            thread = threading.Thread(target=start_process)  # Use threading instead of multiprocessing
            thread.daemon = True  # Make thread a daemon
            thread.start()  # Start the thread
            return "Logged in! Process started."
        except Exception as e:
            return f"Error! <br> {str(e)}"
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
