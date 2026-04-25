
from flask import Flask, request, abort
import threading
import subprocess
import time

app = Flask(__name__)

def run_subprocess():
    # Starting the subprocess
    p = subprocess.Popen(['/path/to/file.py'])
    print("Process created: PID =", p.pid)  # Logging the PID

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
            # Using threading to run the subprocess
            thread = threading.Thread(target=run_subprocess)
            thread.daemon = True  # This ensures the thread will exit when the main program does
            thread.start()

            return "Logged in! The process is running in the background."
        except Exception as e:
            return "Error! <br> " + str(e)
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
