
from flask import Flask, request, abort
import subprocess as sub
import sys

app = Flask(__name__)

def f():
    p = sub.Popen(['python', '/path/to/file.py'])  # Change the command as needed
    print("Process created: PID {}".format(p.pid))  # Log the PID

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
            f()  # Call the function to start the subprocess directly
            return "Logged in!"
        except Exception as e:
            return "Error! <br> {}".format(str(e))
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
