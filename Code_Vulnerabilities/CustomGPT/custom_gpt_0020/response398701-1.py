
from flask import Flask, request, abort
import subprocess
import multiprocessing as mp
import time

app = Flask(__name__)

def start_process():
    # Start the subprocess in a separate function
    subprocess.Popen(['python', '/path/to/file.py'])  # Adjust Python interpreter path if necessary

@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == "GET":
        # Return an HTML form with a 'Login' button
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
            # Start the process without waiting for it
            m = mp.Process(target=start_process)
            m.start()
            return "Logged in!"
        except Exception as e:
            return f"Error! <br> {str(e)}"
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
