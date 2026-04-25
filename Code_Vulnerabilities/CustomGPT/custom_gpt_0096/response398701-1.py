
from flask import Flask, request, abort
import subprocess
import threading

app = Flask(__name__)

# Function to run your subprocess
def run_subprocess():
    p = subprocess.Popen(['python', '/path/to/file.py'])  # Use 'python' for correct execution
    print("Process created with PID: " + str(p.pid))  # Log process ID

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
            thread.daemon = True  # Allow thread to exit when the main program does
            thread.start()
            return "Logged in! Process started."
        except Exception as e:
            return "Error! <br> " + str(e)
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
