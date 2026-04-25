
from flask import Flask, request, abort
import subprocess
import threading

app = Flask(__name__)

def start_daemon():
    p = subprocess.Popen(['python', '/path/to/file.py'])  # Make sure to use the correct Python executable
    print(f"Process created with PID: {p.pid}")

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
            thread = threading.Thread(target=start_daemon)
            thread.daemon = True  # This allows the thread to exit when the main program does
            thread.start()
            return "Logged in!"
        except Exception as e:
            return "Error! <br> " + str(e)
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
