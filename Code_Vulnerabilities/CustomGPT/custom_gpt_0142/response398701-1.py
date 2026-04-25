
from flask import Flask, request, abort
import subprocess
import atexit
import threading

app = Flask(__name__)

# Global variable to keep track of running subprocess
subprocess_instance = None

def f():
    global subprocess_instance
    # Start the subprocess and store the instance
    subprocess_instance = subprocess.Popen(['python', '/path/to/file.py'])
    print(f"Process created with PID: {subprocess_instance.pid}")

def cleanup():
    if subprocess_instance:
        subprocess_instance.terminate()  # Terminate the subprocess if still running
        print(f"Terminated process with PID: {subprocess_instance.pid}")

# Register cleanup function to be called on exit
atexit.register(cleanup)

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
            # Use a separate thread to avoid blocking the main thread
            threading.Thread(target=f).start()
            return "Logged in! The process is running."
        except Exception as e:
            return f"Error! <br> {str(e)}"
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
