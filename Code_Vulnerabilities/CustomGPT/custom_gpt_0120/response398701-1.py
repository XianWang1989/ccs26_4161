
from flask import Flask, request, abort
import threading
import subprocess
import time

app = Flask(__name__)

def run_subprocess():
    # Run the subprocess
    p = subprocess.Popen(['/path/to/file.py'])
    print(f"Process created with PID: {p.pid}")
    p.wait()  # Wait for the process to finish if needed

@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == "GET":
        # Return an HTML form with a 'Login' button
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
            # Start the subprocess in a new thread
            thread = threading.Thread(target=run_subprocess)
            thread.daemon = True  # Allows the thread to exit when the main program does
            thread.start()
            return "Logged in!"
        except Exception as e:
            return f"Error! <br> {str(e)}"
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
