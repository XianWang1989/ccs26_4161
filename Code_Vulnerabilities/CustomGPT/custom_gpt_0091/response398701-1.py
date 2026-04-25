
from flask import Flask, request, abort
import subprocess
import threading

app = Flask(__name__)

def run_subprocess():
    # Start the subprocess
    p = subprocess.Popen(['python', '/path/to/file.py'])
    print("Process created with PID:", p.pid)

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
            # Start a new thread that runs the subprocess
            thread = threading.Thread(target=run_subprocess)
            thread.daemon = True  # This ensures the thread exits when the main program does
            thread.start()        # Start the thread
            return "Logged in!"
        except Exception as e:
            return "Error! <br> " + str(e)
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
