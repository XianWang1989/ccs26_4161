
from flask import Flask, request, abort
import subprocess
import multiprocessing
import time

app = Flask(__name__)

def run_subprocess():
    # Adjust the command to your actual script
    subprocess.Popen(['python', '/path/to/file.py'])

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
            # Start a new process for the subprocess
            process = multiprocessing.Process(target=run_subprocess)
            process.start()
            return "Logged in and process is running!"
        except Exception as e:
            return f"Error! <br> {str(e)}"
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
