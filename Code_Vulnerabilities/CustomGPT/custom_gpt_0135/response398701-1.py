
from flask import Flask, request, abort
import subprocess
import threading
import time

app = Flask(__name__)

def run_daemon():
    # This runs the external script as a subprocess
    process = subprocess.Popen(['python', '/path/to/your_script.py'])
    print("Process started with PID:", process.pid)

@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == "GET":
        # Return an HTML form with a 'Login' button
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
            # Start a thread that runs the daemon
            thread = threading.Thread(target=run_daemon)
            thread.daemon = True  # This allows the thread to exit when the main program does
            thread.start()

            time.sleep(1)  # Wait a moment to ensure the process has started
            return "Logged in!"
        except Exception as e:
            return "Error!<br>" + str(e)
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
