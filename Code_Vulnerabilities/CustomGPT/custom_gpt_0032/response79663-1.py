
import threading

# Create a dictionary to hold username to Boolean mapping
user_status = {}
# Create a Lock for thread safety
lock = threading.Lock()

def update_user_status(username, status):
    with lock:  # Acquire the lock before updating the dictionary
        user_status[username] = status
        print(f"Updated {username} to {status}")

def get_user_status(username):
    with lock:  # Acquire the lock before reading from the dictionary
        return user_status.get(username, False)

# Example usage in a threaded environment
def handle_request(username, status):
    update_user_status(username, status)
    current_status = get_user_status(username)
    print(f"{username}'s current status: {current_status}")

# Simulating multiple threads updating the dictionary
threads = [
    threading.Thread(target=handle_request, args=('user1', True)),
    threading.Thread(target=handle_request, args=('user2', False)),
    threading.Thread(target=handle_request, args=('user1', False)),
]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
