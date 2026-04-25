
from flask import Flask, request, abort
import subprocess
import threading

app = Flask(__name__)

def run_daemon():
    # Replace with your actual script path
    subprocess.Popen(['python', '/path/to/file.py']) 
    print("Daemon process started.")

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
            # Create and start a new thread for the daemon
            thread = threading.Thread(target=run_daemon)
            thread.daemon = True  # Set the thread as a daemon
            thread.start()
            return "Logged in! The process is running in the background."
        except Exception as e:
            return f"Error! <br> {str(e)}"
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
