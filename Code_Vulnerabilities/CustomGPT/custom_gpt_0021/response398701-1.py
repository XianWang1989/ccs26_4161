
from flask import Flask, request, abort
import subprocess
import threading

app = Flask(__name__)

def run_process():
    # Start the subprocess
    p = subprocess.Popen(["/path/to/file.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(f"Process started with PID: {p.pid}")

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
            # Use a thread to run the process
            thread = threading.Thread(target=run_process)
            thread.start()  # Start the thread
            return "Logged in!"
        except Exception as e:
            return f"Error! <br> {str(e)}"
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
