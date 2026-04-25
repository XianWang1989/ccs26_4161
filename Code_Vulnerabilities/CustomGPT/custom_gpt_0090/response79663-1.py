
import threading

class ThreadSafeDictionary:
    def __init__(self):
        self.lock = threading.Lock()
        self.data = {}

    def update(self, username, value):
        with self.lock:
            self.data[username] = value

    def get(self, username):
        with self.lock:
            return self.data.get(username)

# Example usage
thread_safe_dict = ThreadSafeDictionary()

def update_user_status(username, value):
    thread_safe_dict.update(username, value)

# Example threads updating the dictionary
threads = []
for i in range(5):
    t = threading.Thread(target=update_user_status, args=(f'user{i}', True))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

# Accessing the dictionary
print(thread_safe_dict.data)
