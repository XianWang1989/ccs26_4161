
import threading

# Shared dictionary
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
    threads = []
    for i in range(20):
        # Simulating 20 different users
        username = f"user{i}"
        status = i % 2 == 0  # Example status (True/False)
        thread = threading.Thread(target=handle_request, args=(username, status))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Final user status:", user_status)
