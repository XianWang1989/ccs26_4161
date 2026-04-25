
from flask import Flask, request, abort
import subprocess
import threading

app = Flask(__name__)

# Function to run the subprocess
def run_subprocess():
    # Start the subprocess
    p = subprocess.Popen(['python', '/path/to/file.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(f"Process created with PID: {p.pid}")

# Route for handling requests
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
            # Run the subprocess in a separate thread
            thread = threading.Thread(target=run_subprocess)
            thread.daemon = True  # This makes the thread exit when the main program does
            thread.start()
            return "Logged in! Process is now running."
        except Exception as e:
            return f"Error! <br> {str(e)}"
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
