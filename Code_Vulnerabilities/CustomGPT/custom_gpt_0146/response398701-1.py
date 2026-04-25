
from flask import Flask, request, abort
import subprocess
import multiprocessing as mp
import time

app = Flask(__name__)

def f():
    # This method will run your subprocess
    p = subprocess.Popen(['/path/to/file.py'])
    print("Process created with PID: {}".format(p.pid))  # Log the process ID

@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == "GET":
        # Display an HTML form with a 'Login' button
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
            # Create a new process that runs the f() function
            m = mp.Process(target=f)
            m.start()  # Start the process
            # No need for sleep, we aren't dependent on the subprocess completion
            return "Logged in! Process started."
        except Exception as e:
            return "Error! <br> {}".format(str(e))
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True, threaded=True)  # Use threaded mode
