
from flask import Flask, request, abort
import subprocess
import threading

app = Flask(__name__)

def run_process():
    # Start the subprocess to run the target Python script
    subprocess.Popen(['python', '/path/to/file.py'])

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
            # Start the process in a separate thread
            thread = threading.Thread(target=run_process)
            thread.start()
            return "Logged in!"
        except Exception as e:
            return "error! <br> " + str(e)
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
