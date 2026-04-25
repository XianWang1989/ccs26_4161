
from flask import Flask, request, abort
import subprocess
import multiprocessing as mp

app = Flask(__name__)

def f():
    # Start your long-running process here
    process = subprocess.Popen(['python', '/path/to/file.py'])
    print(f"Process created with PID: {process.pid}")

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
            # Create and start a new process to run the f() function
            m = mp.Process(target=f)
            m.start()  # No need to daemonize; we just start it
            return "Logged in!"
        except Exception as e:
            return f"Error! <br> {str(e)}"
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
