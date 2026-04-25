
import threading

# Initialize a dictionary to store username and their associated Boolean values
user_status = {}
# Create a lock for thread safety
lock = threading.Lock()

def update_user_status(username, status):
    with lock:  # Acquire the lock
        user_status[username] = status  # Update the dictionary safely

def get_user_status(username):
    with lock:  # Acquire the lock for reading
        return user_status.get(username, None)

# Example usage
if __name__ == "__main__":
    # Update users in separate threads
    threads = []
    for i in range(10):
        username = f"user_{i}"
        status = i % 2 == 0  # Example status (True/False)
        t = threading.Thread(target=update_user_status, args=(username, status))
        threads.append(t)
        t.start()

    # Wait for all threads to complete
    for t in threads:
        t.join()

    # Print final user statuses
    print(user_status)
