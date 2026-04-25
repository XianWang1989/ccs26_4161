
import threading

# Initialize a Lock
lock = threading.Lock()

# Your shared dictionary
user_status = {}

def update_user_status(username, status):
    # Acquire the lock before updating the dictionary
    with lock:
        user_status[username] = status
        print(f"Updated {username}'s status to {status}")

def get_user_status(username):
    # Acquire the lock while reading the dictionary
    with lock:
        return user_status.get(username, None)

# Example usage
def thread_function(username, status):
    update_user_status(username, status)
    current_status = get_user_status(username)
    print(f"{username}'s current status: {current_status}")

# Simulating multiple threads
threads = []
for i in range(5):
    username = f"user{i}"
    status = True if i % 2 == 0 else False
    thread = threading.Thread(target=thread_function, args=(username, status))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()
