
from flask import Flask, request, abort
import subprocess as sub
import multiprocessing as mp

app = Flask(__name__)

def run_subprocess():
    # Start the long-running subprocess here
    p = sub.Popen(['python', '/path/to/file.py'])  # Update with actual script
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
            # Create and start a non-daemon process
            m = mp.Process(target=run_subprocess)
            m.start()  # Start the process
            return "Logged in!"
        except Exception as e:
            return "Error! <br> " + str(e)
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
