
import threading
from flask import Flask, request

app = Flask(__name__)

# Thread-safe dictionary with a lock
user_status = {}
lock = threading.Lock()

@app.route('/update_status', methods=['POST'])
def update_status():
    username = request.json.get('username')
    status = request.json.get('status')  # Expecting a Boolean value

    if username is None or status is None:
        return "Username and status are required!", 400

    # Use the lock to ensure thread-safe access to the dictionary
    with lock:
        user_status[username] = status

    return f"Updated status for {username} to {status}", 200

@app.route('/get_status/<username>', methods=['GET'])
def get_status(username):
    # Use the lock for reading
    with lock:
        status = user_status.get(username, None)

    if status is None:
        return f"No status found for {username}", 404

    return f"Status for {username}: {status}", 200

if __name__ == "__main__":
    app.run(threaded=True)  # Enable threaded mode to handle requests in parallel
