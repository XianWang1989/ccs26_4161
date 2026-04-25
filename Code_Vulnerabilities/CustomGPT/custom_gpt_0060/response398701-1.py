
from flask import Flask, request, abort
import multiprocessing as mp
import subprocess
import sys
import time

app = Flask(__name__)

def run_subprocess():
    # Start your long-running subprocess here
    p = subprocess.Popen(['python', '/path/to/your_script.py'])
    print(f"Process created with PID: {p.pid}")  # Log the subprocess ID

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
            # Use 'mp.Process' to run the subprocess in a separate process
            process = mp.Process(target=run_subprocess)
            process.start()  # Start the process

            # Return a response immediately
            return "Logged in!"
        except Exception as e:
            return f"Error! <br> {str(e)}"
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
