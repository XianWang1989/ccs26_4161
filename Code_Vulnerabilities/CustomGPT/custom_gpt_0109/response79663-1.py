
import threading

# Create a dictionary to store username -> Boolean
user_status = {}
lock = threading.Lock()

def update_user_status(username, status):
    """Updates the user status in a thread-safe manner."""
    with lock:  # Acquire the lock
        user_status[username] = status  # Update the dictionary

def get_user_status(username):
    """Retrieves the user status in a thread-safe manner."""
    with lock:  # Acquire the lock
        return user_status.get(username, None)  # Get the status

# Example usage
if __name__ == "__main__":
    # Simulate updating user statuses from multiple threads
    def simulate_updates():
        usernames = ['alice', 'bob', 'charlie']
        for username in usernames:
            status = True  # Example status
            update_user_status(username, status)

    threads = []
    for i in range(5):  # Create 5 threads
        thread = threading.Thread(target=simulate_updates)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()  # Wait for all threads to finish

    print(user_status)  # Output the final user statuses
