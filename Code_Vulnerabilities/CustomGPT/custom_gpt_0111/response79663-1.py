
import threading

# Shared dictionary
user_status = {}
# Lock for thread safety
lock = threading.Lock()

def update_user_status(username, status):
    with lock:  # Acquire the lock before modifying the dictionary
        user_status[username] = status

def get_user_status(username):
    with lock:  # Acquire the lock before accessing the dictionary
        return user_status.get(username, False)

# Example usage
def handle_request(username, status):
    update_user_status(username, status)
    print(f"User {username} status updated to {status}")

# Simulating concurrent requests
threads = []
for i in range(10):
    t = threading.Thread(target=handle_request, args=(f'user{i}', i % 2 == 0))
    threads.append(t)
    t.start()

for t in threads:
    t.join()  # Wait for all threads to finish

print(user_status)  # Display final user status
