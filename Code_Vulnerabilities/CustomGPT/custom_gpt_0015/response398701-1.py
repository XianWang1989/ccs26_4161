
from flask import Flask, request, abort
import subprocess
import threading

app = Flask(__name__)

def run_subprocess():
    # Replace with the actual command you want to run as a subprocess
    subprocess.Popen(['/path/to/file.py'])
    print("Process started.")

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
            # Use threading to run the subprocess without blocking the response
            thread = threading.Thread(target=run_subprocess)
            thread.start()
            return "Logged in!"
        except Exception as e:
            return "Error! <br> " + str(e)
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
