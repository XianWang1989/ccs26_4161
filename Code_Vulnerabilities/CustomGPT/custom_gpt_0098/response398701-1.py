
from flask import Flask, request, abort
import subprocess
import threading

app = Flask(__name__)

def run_process():
    # Start the subprocess in a separate thread
    subprocess.Popen(['/path/to/file.py'])
    print("Process started")

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
            thread = threading.Thread(target=run_process)
            thread.daemon = True  # ensures the thread will close when the main program exits
            thread.start()
            return "Logged in!"
        except Exception as e:
            return f"Error! <br> {str(e)}"
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
