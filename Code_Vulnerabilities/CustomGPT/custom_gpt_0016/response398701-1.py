
from flask import Flask, request, abort
import subprocess

app = Flask(__name__)

def start_daemon_process():
    # Modify the command to point to your actual script
    subprocess.Popen(['python', '/path/to/file.py'], start_new_session=True)

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
            # Start the process
            start_daemon_process()
            return "Logged in! The process has been started."
        except Exception as e:
            return f"Error! <br> {str(e)}"
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
