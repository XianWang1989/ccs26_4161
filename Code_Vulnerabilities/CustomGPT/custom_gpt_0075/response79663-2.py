
import threading

# Creating a thread-safe dictionary
user_status = {}
lock = threading.Lock()

def update_status(username, status):
    with lock:  # Automatically acquire and release the lock
        user_status[username] = status

def get_status(username):
    with lock:
        return user_status.get(username, False)
