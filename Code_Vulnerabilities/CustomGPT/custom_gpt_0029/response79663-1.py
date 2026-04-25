
import threading

# Initialize the dictionary and a lock
user_status = {}
lock = threading.Lock()

def update_user_status(username, status):
    with lock:
        user_status[username] = status

def get_user_status(username):
    with lock:
        return user_status.get(username, False)

# Example usage in a thread
def handle_request(username, status):
    update_user_status(username, status)
    current_status = get_user_status(username)
    print(f"{username}: {current_status}")

# Sample threads simulating requests
threads = []
for i in range(10):
    t = threading.Thread(target=handle_request, args=(f'user{i}', i % 2 == 0))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
