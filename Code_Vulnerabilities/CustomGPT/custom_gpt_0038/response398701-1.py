
from flask import Flask, request, abort
import subprocess
import threading

app = Flask(__name__)

def run_subprocess():
    p = subprocess.Popen(['python', '/path/to/file.py'])
    print(f"Process created with PID: {p.pid}")  # logs the process ID

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
            # Use threading instead of multiprocessing for lightweight tasks
            thread = threading.Thread(target=run_subprocess)
            thread.daemon = True  # Ensure it doesn’t block the program exiting
            thread.start()  # Starts the thread

            return "Logged in!"
        except Exception as e:
            return f"Error! <br> {str(e)}"
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
