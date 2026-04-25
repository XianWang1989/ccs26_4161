
from flask import Flask, request, abort
import subprocess
import threading

app = Flask(__name__)

def run_subprocess():
    # Start the target script as a subprocess
    p = subprocess.Popen(['python', '/path/to/file.py'])
    print(f"Process created with PID: {p.pid}")

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
            # Use threading to avoid blocking and allow the server to respond
            thread = threading.Thread(target=run_subprocess)
            thread.daemon = True  # Daemonize the thread
            thread.start()
            return "Logged in! The process is running."
        except Exception as e:
            return f"Error! <br> {str(e)}"
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
