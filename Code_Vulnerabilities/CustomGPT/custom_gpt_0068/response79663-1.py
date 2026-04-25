
import threading

# Global dictionary to hold username -> Boolean values
user_status = {}
# Create a lock object
lock = threading.Lock()

def update_user_status(username, status):
    """Update the user status in a thread-safe manner."""
    with lock:  # Acquire the lock before accessing the shared resource
        user_status[username] = status
        print(f"Updated {username} status to {status}")

def worker(username, status):
    """Simulate a worker thread updating user status."""
    update_user_status(username, status)

# Example usage:
if __name__ == "__main__":
    # Create threads
    threads = []
    usernames = ["user1", "user2", "user3"]
    statuses = [True, False, True]

    for username, status in zip(usernames, statuses):
        thread = threading.Thread(target=worker, args=(username, status))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    # Print final user statuses
    print("Final user status dictionary:", user_status)
