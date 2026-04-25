
from flask import Flask, request, abort
import subprocess
import threading

app = Flask(__name__)

def run_daemon():
    p = subprocess.Popen(['/path/to/file.py'])
    print("Process created with PID: " + str(p.pid))  # prints to log

@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == "GET":
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
            daemon_thread = threading.Thread(target=run_daemon)
            daemon_thread.daemon = True  # Daemonize thread
            daemon_thread.start()
            return "Logged in!"
        except Exception as e:
            return "Error! <br> " + str(e)
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
