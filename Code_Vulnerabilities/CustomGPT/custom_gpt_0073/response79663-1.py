
import threading

class SafeDict:
    def __init__(self):
        self.lock = threading.Lock()
        self.data = {}

    def update(self, username, value):
        with self.lock:
            self.data[username] = value

    def get(self, username):
        with self.lock:
            return self.data.get(username)

# Usage
safe_dict = SafeDict()

def handle_request(username, value):
    safe_dict.update(username, value)
    print(f"Updated {username} to {value}")

# Example of handling requests in different threads
threads = []
for i in range(5):
    t = threading.Thread(target=handle_request, args=(f"user{i}", True))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

# Accessing the dictionary safely
print(safe_dict.data)
