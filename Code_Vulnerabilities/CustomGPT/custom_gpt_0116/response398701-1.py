
from flask import Flask, request, abort
import threading
import subprocess
import time

app = Flask(__name__)

def start_daemon():
    # Start the subprocess
    p = subprocess.Popen(['python', '/path/to/file.py'])
    print(f"Process created: {p.pid}")  # Log the process ID

@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == "GET":
        # Return HTML form
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
            # Create and start the thread
            thread = threading.Thread(target=start_daemon)
            thread.daemon = True  # Daemonize the thread
            thread.start()  # Start the thread
            return "Logged in!"  # Respond immediately
        except Exception as e:
            return f"Error! <br> {str(e)}"
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
