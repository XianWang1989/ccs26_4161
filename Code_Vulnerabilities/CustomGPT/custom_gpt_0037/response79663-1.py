
import threading

# Shared dictionary
user_status = {}
# Lock for thread safety
lock = threading.Lock()

def update_user_status(username, status):
    with lock:  # Acquiring the lock
        user_status[username] = status
        print(f"Updated {username}: {status}")

def handle_request(username, status):
    # Simulating request handling by updating user status
    update_user_status(username, status)

# Example usage with threads
threads = []
for i in range(10):  # Simulating multiple requests
    username = f"user_{i}"
    status = i % 2 == 0  # Example status
    thread = threading.Thread(target=handle_request, args=(username, status))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print(user_status)
