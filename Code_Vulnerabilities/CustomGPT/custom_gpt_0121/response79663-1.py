
import threading

# Create a shared dictionary and a lock
user_status = {}
lock = threading.Lock()

def update_user_status(username, status):
    with lock:  # Acquire the lock before modifying the dictionary
        user_status[username] = status
        print(f"Updated {username} to {status}")

def get_user_status(username):
    with lock:  # Ensure safe read access
        return user_status.get(username, None)

# Example usage with threads
def simulate_request(username, status):
    update_user_status(username, status)
    print(f"{username} status: {get_user_status(username)}")

# Simulating concurrent requests
threads = []
for i in range(5):
    threads.append(threading.Thread(target=simulate_request, args=(f"user{i}", True)))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print("Final user statuses:", user_status)
