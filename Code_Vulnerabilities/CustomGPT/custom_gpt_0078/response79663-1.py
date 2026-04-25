
import threading

# Initialize the dictionary and a lock
user_status = {}
lock = threading.Lock()

def update_user_status(username, status):
    # Acquire the lock before modifying the dictionary
    with lock:
        user_status[username] = status

def get_user_status(username):
    # Acquire the lock to read the value safely
    with lock:
        return user_status.get(username, False)  # Default to False if user not found

# Example of how to use these functions in threads
def handle_request(username, status):
    update_user_status(username, status)
    print(f"Status for {username}: {get_user_status(username)}")

# Simulating multiple threads updating the dictionary
threads = []
for i in range(20):
    username = f"user{i}"
    status = True if i % 2 == 0 else False
    thread = threading.Thread(target=handle_request, args=(username, status))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()
