
from flask import Flask, request, abort
import subprocess
import threading

app = Flask(__name__)

def run_daemon():
    # Start the subprocess
    subprocess.Popen(['/path/to/file.py'])

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
            # Use threading to run the daemon without blocking Flask
            thread = threading.Thread(target=run_daemon)
            thread.daemon = True  # Mark the thread as daemon
            thread.start()  # Start the thread
            return "Logged in and daemon started!"
        except Exception as e:
            return "Error! <br> " + str(e)
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
