
from flask import Flask, request, abort
import threading
import subprocess
import time

app = Flask(__name__)

def f():
    p = subprocess.Popen(['python', '/path/to/file.py'])
    print("Process created with PID:", p.pid)

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
            thread = threading.Thread(target=f)
            thread.daemon = True
            thread.start()
            time.sleep(1)  # Optional: allow time for the subprocess to start
            return "Logged in!"
        except Exception as e:
            return "Error! <br> " + str(e)
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
