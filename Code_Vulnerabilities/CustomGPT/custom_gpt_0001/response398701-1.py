
from flask import Flask, request, abort
import subprocess
import threading

app = Flask(__name__)

def run_daemon_process():
    # Start the long-running subprocess
    p = subprocess.Popen(['python', '/path/to/file.py'])
    print(f"Process created with PID: {p.pid}")  # Log the PID

@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == "GET":
        # Return an HTML form with a 'Login' button
        return """
        <!DOCTYPE html>
        <html>
          <head>
          </head>
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
            # Create and start a thread to run the daemon process
            daemon_thread = threading.Thread(target=run_daemon_process)
            daemon_thread.daemon = True  # Make the thread a daemon
            daemon_thread.start()
            return "Logged in! The process is running."
        except Exception as e:
            return f"error! <br> {str(e)}"
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
