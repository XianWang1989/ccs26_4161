
import threading

# Initialize the dictionary and a lock
user_status = {}
lock = threading.Lock()

def update_user_status(username, status):
    with lock:  # Acquire lock before modifying the dictionary
        user_status[username] = status
        print(f"Updated: {username} -> {status}")

def fetch_user_status(username):
    with lock:  # Acquire lock before reading from the dictionary
        return user_status.get(username, False)

# Example usage
def thread_function(username, status):
    update_user_status(username, status)
    print(f"{username} status: {fetch_user_status(username)}")

# Simulating multiple threads
threads = []
for i in range(5):
    t = threading.Thread(target=thread_function, args=(f"user{i}", True))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
