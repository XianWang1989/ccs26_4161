
import threading

# Initialize the dictionary and a lock
user_status = {}
lock = threading.Lock()

def update_user_status(username, status):
    with lock:  # Acquire the lock
        user_status[username] = status  # Update the dictionary
        print(f"Updated {username}: {status}")

# Example usage
def thread_function(username, status):
    update_user_status(username, status)

# Simulate multiple threads
threads = []
for i in range(10):
    t = threading.Thread(target=thread_function, args=(f'user{i}', i % 2 == 0))
    threads.append(t)
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()

print(user_status)  # Print the final dictionary
