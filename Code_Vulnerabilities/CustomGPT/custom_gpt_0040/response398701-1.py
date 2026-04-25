
from flask import Flask, request, abort
import subprocess
import threading
import time

app = Flask(__name__)

def run_subprocess():
    # Replace this with the actual path to your Python script or command
    p = subprocess.Popen(['python', '/path/to/file.py'])
    print("Process started with PID:", p.pid)

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
            # Start a new thread for the subprocess
            thread = threading.Thread(target=run_subprocess)
            thread.daemon = True  # Allow the thread to exit when the main program does
            thread.start()  # Start the thread
            time.sleep(1)  # Optional: Wait a moment to ensure the subprocess starts
            return "Logged in!"
        except Exception as e:
            return f"Error! <br> {str(e)}"
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
