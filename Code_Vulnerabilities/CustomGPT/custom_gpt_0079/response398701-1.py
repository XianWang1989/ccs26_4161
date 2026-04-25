
from flask import Flask, request, abort
import subprocess
import multiprocessing as mp

app = Flask(__name__)

def run_subprocess():
    # Start the subprocess
    subprocess.Popen(['python', '/path/to/file.py'])
    print("Subprocess started.")

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
            # Start the subprocess in a new daemon process
            processes = mp.Process(target=run_subprocess)
            processes.daemon = True
            processes.start()
            return "Logged in! The process is running."
        except Exception as e:
            return f"Error! <br> {str(e)}"
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
