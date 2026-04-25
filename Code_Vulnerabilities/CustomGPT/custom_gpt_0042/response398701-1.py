
from flask import Flask, request, abort
import subprocess
import threading
import sys

app = Flask(__name__)

# Function to run the subprocess
def run_subprocess():
    p = subprocess.Popen(['python', '/path/to/file.py'])  # Adjust the command as needed
    print("Process created with PID:", p.pid)  # Prints to log

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
            # Create and start a thread to run the subprocess
            thread = threading.Thread(target=run_subprocess)
            thread.start()  # Start the thread
            return "Logged in!"
        except Exception as e:
            return "Error! <br> " + str(e)

    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
