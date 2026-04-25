
from flask import Flask, request, abort
import subprocess
import threading

app = Flask(__name__)

def run_subprocess():
    # Start the subprocess
    p = subprocess.Popen(['/path/to/file.py'])
    print("Process created with PID: " + str(p.pid))

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
        try:
            # Start the subprocess in a new thread
            thread = threading.Thread(target=run_subprocess)
            thread.start()  # Start the thread
            return "Logged in and process started!"
        except Exception as e:
            return "Error! <br> " + str(e)
    else:
        abort(401)

if __name__ == '__main__':
    app.run(debug=True)
