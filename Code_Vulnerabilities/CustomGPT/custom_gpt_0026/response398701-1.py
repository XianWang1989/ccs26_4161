
from flask import Flask, request, abort
import subprocess
import multiprocessing as mp

app = Flask(__name__)

def run_daemon():
    # Start your subprocess here
    subprocess.Popen(['python', '/path/to/file.py'])
    print("Daemon process started.")

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
            # Start a new process that runs the daemon
            m = mp.Process(target=run_daemon)
            m.start()
            return "Logged in! Daemon running."
        except Exception as e:
            return f"Error! <br> {str(e)}"
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
