
from flask import Flask, request, abort
import subprocess
import threading

app = Flask(__name__)

def start_process():
    """Function to start the subprocess."""
    p = subprocess.Popen(['/path/to/file.py'])
    print(f"Process created with PID: {p.pid}")  # prints to log

@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == "GET":
        # return an HTML form with a 'Login' button
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
            # Start a new thread to run the process
            process_thread = threading.Thread(target=start_process)
            process_thread.start()
            return "Logged in!"
        except Exception as e:
            return f"Error! <br> {e}"
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
