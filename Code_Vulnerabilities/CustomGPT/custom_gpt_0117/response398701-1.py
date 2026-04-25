
from flask import Flask, request, abort
import subprocess
import threading

app = Flask(__name__)

def run_subprocess():
    # Start the subprocess and detach it
    subprocess.Popen(['python', '/path/to/file.py'], 
                     stdout=subprocess.DEVNULL, 
                     stderr=subprocess.DEVNULL)

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
        # Run the subprocess in a separate thread
        thread = threading.Thread(target=run_subprocess)
        thread.daemon = True  # This allows the thread to exit when the main program exits
        thread.start()
        return "Logged in!"
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
