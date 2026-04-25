
import threading

# Shared dictionary
user_status = {}
# Create a lock
lock = threading.Lock()

def update_user_status(username, status):
    with lock:
        user_status[username] = status
        print(f"Updated {username} status to {status}")

def worker(username, status):
    # Simulate some work
    update_user_status(username, status)

# Example usage
if __name__ == "__main__":
    threads = []
    users = [("user1", True), ("user2", False), ("user3", True)]

    for username, status in users:
        t = threading.Thread(target=worker, args=(username, status))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(user_status)
