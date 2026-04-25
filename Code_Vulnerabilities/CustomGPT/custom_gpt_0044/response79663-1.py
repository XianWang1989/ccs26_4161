
import threading

# Initialize the dictionary and a lock
user_status = {}
lock = threading.Lock()

def update_user_status(username, status):
    with lock:  # Acquire the lock before modifying the dictionary
        user_status[username] = status
        print(f"Updated {username} to {status}")

def handle_request(username, status):
    # Simulate handling a request and updating user status
    update_user_status(username, status)

# Example usage
if __name__ == "__main__":
    # Creating threads to simulate requests
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

    print(user_status)
