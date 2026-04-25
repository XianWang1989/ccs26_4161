
from flask import Flask, request, abort
import subprocess
import multiprocessing as mp
import sys
import time

app = Flask(__name__)

def run_subprocess():
    # Here you'd run your long-running process
    # Using a placeholder command for demonstration
    subprocess.Popen(['/path/to/file.py'])
    print(f"Subprocess started with PID: {subprocess.Popen.pid}")

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
        # Create and start the subprocess
        try:
            process = mp.Process(target=run_subprocess)
            process.start()  # Start the process
            # Don't call process.join() here, as it will block until the process finishes
            return "Logged in! The long-running process has been started."
        except Exception as e:
            return f"Error! <br> {str(e)}"
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
