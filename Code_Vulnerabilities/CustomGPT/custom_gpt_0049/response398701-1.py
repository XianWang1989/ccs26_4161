
from flask import Flask, request, abort
import subprocess
import sys
import multiprocessing as mp

app = Flask(__name__)

def run_subprocess():
    # Replace with the path to your script
    subprocess.Popen(['python', '/path/to/file.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

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
            # Start subprocess in a separate process
            process = mp.Process(target=run_subprocess)
            process.start()
            return "Logged in! Process started."
        except Exception as e:
            return f"Error! <br> {str(e)}"
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
