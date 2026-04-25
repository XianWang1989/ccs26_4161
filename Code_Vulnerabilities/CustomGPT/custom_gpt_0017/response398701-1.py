
from flask import Flask, request, abort
import subprocess
import threading

app = Flask(__name__)

def run_subprocess():
    # Start the subprocess and let it run independently
    p = subprocess.Popen(['python', '/path/to/file.py'])
    print("Process created with PID:", p.pid)  # Log process ID

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
            # Using threading to run subprocess without blocking the response
            thread = threading.Thread(target=run_subprocess)
            thread.daemon = True
            thread.start()
            return "Logged in!"
        except Exception as e:
            return "Error! <br> " + str(e)
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
