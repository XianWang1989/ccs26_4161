
from flask import Flask, request, abort
import subprocess
import threading

app = Flask(__name__)

def run_subprocess():
    p = subprocess.Popen(['python', '/path/to/file.py'])  # Update with your script path
    print(f"Process created with PID: {p.pid}")

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
            thread = threading.Thread(target=run_subprocess)
            thread.daemon = True  # Allow the thread to exit when the main program does
            thread.start()
            return "Logged in! Your process is running."
        except Exception as e:
            return f"Error! <br> {str(e)}"
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
