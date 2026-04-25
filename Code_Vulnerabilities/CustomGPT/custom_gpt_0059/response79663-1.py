
import threading

# Dictionary to hold username -> Boolean mappings
user_status = {}
# Lock for thread safety
lock = threading.Lock()

def update_user_status(username, status):
    with lock:
        user_status[username] = status
        print(f'Updated: {username} -> {status}')

def get_user_status(username):
    with lock:
        return user_status.get(username, None)

# Example usage
if __name__ == "__main__":
    # Simulate updating user statuses in multiple threads
    threads = []
    for i in range(5):
        t = threading.Thread(target=update_user_status, args=(f'user_{i}', True))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    # Check the final state of the dictionary
    print(user_status)
