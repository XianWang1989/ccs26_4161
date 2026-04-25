
from flask import Flask, request, abort
import threading
import subprocess
import time

app = Flask(__name__)

def run_process():
    # Trigger the subprocess here
    p = subprocess.Popen(['python', '/path/to/file.py'])  # Adjust the path to your script
    print(f"Process created with PID: {p.pid}")  # Log the PID

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
            # Create and start a new thread to run the subprocess
            thread = threading.Thread(target=run_process)
            thread.daemon = True  # Allow the thread to exit when the main program exits
            thread.start()
            time.sleep(1)  # Optional: wait for a moment to ensure process starts
            return "Logged in!"
        except Exception as e:
            return f"Error! <br> {str(e)}"
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
