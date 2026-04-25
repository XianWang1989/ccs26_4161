
import threading

# Create a dictionary to store username and Boolean values
user_status = {}
lock = threading.Lock()

def update_user_status(username, status):
    with lock:
        user_status[username] = status

def get_user_status(username):
    with lock:
        return user_status.get(username, None)

# Example usage
def handle_request(username, status):
    update_user_status(username, status)
    print(f"Updated {username} to {status}")

# Simulating requests
threads = []
for i in range(10):
    username = f"user{i}"
    status = i % 2 == 0  # Example Boolean status
    thread = threading.Thread(target=handle_request, args=(username, status))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
