
import threading

# Shared dictionary
user_status = {}
# Create a lock
lock = threading.Lock()

def update_status(username, status):
    with lock:
        user_status[username] = status
        print(f"Updated {username} to {status}")

def thread_function(username):
    # Simulating some operations before updating the status
    update_status(username, True)

# Example of starting threads
threads = []
for i in range(20):  # Simulate 20 users
    thread = threading.Thread(target=thread_function, args=(f"user{i+1}",))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print(user_status)
