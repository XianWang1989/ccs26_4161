
from flask import Flask, request, abort
import subprocess
import threading

app = Flask(__name__)

def run_subprocess():
    # Start the daemon process
    subprocess.Popen(['python', '/path/to/file.py'])
    print("Daemon process started.")

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
            # Use threading to run the subprocess
            thread = threading.Thread(target=run_subprocess)
            thread.daemon = True  # Allow thread to exit when the main program does
            thread.start()
            return "Logged in! Daemon process started."
        except Exception as e:
            return f"Error! <br> {str(e)}"
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
