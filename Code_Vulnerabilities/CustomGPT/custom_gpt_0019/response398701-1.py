
from flask import Flask, request, abort
import subprocess
import threading

app = Flask(__name__)

def run_subprocess():
    subprocess.Popen(['python', '/path/to/file.py'], 
                     stdout=subprocess.PIPE, 
                     stderr=subprocess.PIPE)

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
            # Use threading to avoid blocking the Flask response
            thread = threading.Thread(target=run_subprocess)
            thread.daemon = True  # This ensures the thread will not block program exit
            thread.start()
            return "Logged in!"
        except Exception as e:
            return f"error! <br> {str(e)}"
    else:
        abort(401)

if __name__ == "__main__":
    app.run(debug=True)
