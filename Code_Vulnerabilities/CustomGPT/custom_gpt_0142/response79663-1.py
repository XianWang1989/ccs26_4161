
import threading

# Create a dictionary to store usernames and their boolean values
user_status = {}
# Create a lock to manage access to the dictionary
lock = threading.Lock()

def update_user_status(username, status):
    # Acquire the lock before modifying the dictionary
    with lock:
        user_status[username] = status
        print(f"Updated: {username} -> {status}")

def get_user_status(username):
    # Acquire the lock before accessing the dictionary
    with lock:
        return user_status.get(username, None)

# Example usage
def simulate_request(username, status):
    update_user_status(username, status)
    print(f"{username} status: {get_user_status(username)}")

# Simulating multiple requests in threads
threads = []
for i in range(10):
    # Simulate different users with their status
    t = threading.Thread(target=simulate_request, args=(f'user_{i}', i % 2 == 0))
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

# Final state of user_status
print("Final user statuses:", user_status)
