
import threading

# Initialize a dictionary and a lock
user_status = {}
lock = threading.Lock()

def update_user_status(username, status):
    with lock:  # Acquire the lock before updating the dictionary
        user_status[username] = status
        print(f"Updated {username} to {status}. Current status: {user_status}")

def get_user_status(username):
    with lock:  # Acquire the lock before reading the dictionary
        return user_status.get(username, None)

# Example usage in a threaded environment
def handle_request(username, status):
    update_user_status(username, status)
    print(f"{username}'s status is {get_user_status(username)}")

# Simulating multiple threads updating the dictionary
threads = []
for i in range(5):
    t = threading.Thread(target=handle_request, args=(f"user{i}", True))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
