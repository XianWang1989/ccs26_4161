
from flask import Flask, request, abort
import subprocess
import multiprocessing

app = Flask(__name__)

def run_subprocess():
    # Start the subprocess here
    p = subprocess.Popen(['python3', '/path/to/file.py'])  # Adjust command as needed
    print(f"Process created with PID: {p.pid}")  # Log PID

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
            # Create a new process to run the subprocess
            m = multiprocessing.Process(target=run_subprocess)
            m.start()  # Start the process
            return "Logged in! The process is running."
        except Exception as e:
            return f"Error! <br> {str(e)}"
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True, threaded=True)  # Use threaded to handle concurrent requests
