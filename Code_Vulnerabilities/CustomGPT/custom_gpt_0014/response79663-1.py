
import threading

# Create a shared dictionary and a lock
user_status = {}
lock = threading.Lock()

def update_user_status(username, status):
    with lock:  # Acquire the lock
        user_status[username] = status  # Modify the dictionary safely

def get_user_status(username):
    with lock:  # Acquire the lock
        return user_status.get(username, None)  # Safely read the value

# Example usage
def handle_request(username, status):
    update_user_status(username, status)
    print(f"Updated {username} status to {status}")

# Sample threads
threads = []
for user in ['user1', 'user2', 'user3']:
    t = threading.Thread(target=handle_request, args=(user, True))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

# Print final user statuses
print(user_status)
