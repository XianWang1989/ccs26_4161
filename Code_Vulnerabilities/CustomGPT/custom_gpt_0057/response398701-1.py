
from flask import Flask, request, abort
import subprocess
import multiprocessing
import time

app = Flask(__name__)

def f():
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
            m = multiprocessing.Process(target=f)
            m.start()
            return "Logged in!"
        except Exception as e:
            return "error! <br> " + str(e)
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
