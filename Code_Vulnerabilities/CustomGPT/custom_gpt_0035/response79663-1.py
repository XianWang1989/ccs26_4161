
import threading

# Creating a shared dictionary and a lock
shared_dict = {}
lock = threading.Lock()

def update_user_status(username, status):
    with lock:  # Acquire the lock before accessing the dictionary
        shared_dict[username] = status

# Example usage
def handle_request(username, status):
    update_user_status(username, status)
    print(f"Updated {username} to {status}")

# Simulating multiple threads updating the dictionary
threads = []
for i in range(10):
    t = threading.Thread(target=handle_request, args=(f'user{i}', i % 2 == 0))
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

print(shared_dict)
