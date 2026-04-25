
from flask import Flask, request, abort
import subprocess as sub
import threading

app = Flask(__name__)

def run_subprocess():
    p = sub.Popen(['/path/to/file.py'])
    print("Process created with PID: " + str(p.pid))

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
            thread = threading.Thread(target=run_subprocess)  # Create a thread
            thread.start()  # Start the thread
            return "Logged in!"
        except Exception as e:
            return "error! <br> " + str(e)
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
