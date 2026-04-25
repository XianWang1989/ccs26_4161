
import threading

# Create a lock
lock = threading.Lock()

# Shared dictionary
user_status = {}

def update_user_status(username, status):
    with lock:
        user_status[username] = status

# Example usage:
def handle_request(username, status):
    update_user_status(username, status)
    print(f"Updated {username} to {status}")

# Simulating multiple threads updating the dictionary
threads = []
for i in range(10):
    t = threading.Thread(target=handle_request, args=(f'user{i}', i % 2 == 0))
    threads.append(t)
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()

# Final state of the dictionary
print(user_status)
