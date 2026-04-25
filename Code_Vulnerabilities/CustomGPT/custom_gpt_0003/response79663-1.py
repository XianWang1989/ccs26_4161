
import threading

# Initialize a lock
lock = threading.Lock()

# Create a shared dictionary
user_status = {}

def update_user_status(username, status):
    # Acquire the lock before modifying the dictionary
    with lock:
        user_status[username] = status  # Update the dictionary

def get_user_status(username):
    # Acquire the lock before accessing the dictionary
    with lock:
        return user_status.get(username, False)  # Get the status safely

# Example usage
# Simulating multiple threads updating the user_status dictionary
def thread_function(username, status):
    update_user_status(username, status)
    print(f"User: {username}, Status updated to: {status}")

# Create and start threads
threads = []
for i in range(5):
    t = threading.Thread(target=thread_function, args=(f'user{i}', True))
    threads.append(t)
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()

# Display the final user status
print("Final user status:", user_status)
