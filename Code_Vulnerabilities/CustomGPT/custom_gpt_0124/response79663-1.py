
import threading

# Shared dictionary
user_status = {}
# Create a lock object
lock = threading.Lock()

def update_user_status(username, status):
    with lock:  # Acquires the lock
        user_status[username] = status  # Safe update
        print(f"Updated {username} to {status}")

def thread_function(username, status):
    update_user_status(username, status)

# Example of starting threads
if __name__ == "__main__":
    threads = []
    for i in range(20):
        username = f"user{i}"
        status = i % 2 == 0  # Example boolean status
        thread = threading.Thread(target=thread_function, args=(username, status))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()  # Wait for all threads to complete
