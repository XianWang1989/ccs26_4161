
from flask import Flask, request, abort
import subprocess
import multiprocessing

app = Flask(__name__)

def run_daemon():
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
            process = multiprocessing.Process(target=run_daemon)
            process.start()
            return "Logged in!"
        except Exception as e:
            return f"Error! <br> {str(e)}"
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
