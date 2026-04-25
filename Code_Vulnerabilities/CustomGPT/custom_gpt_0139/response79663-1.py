
import threading

# Create a thread-safe dictionary with a lock
class ThreadSafeDict:
    def __init__(self):
        self._lock = threading.Lock()
        self._data = {}

    def set(self, key, value):
        with self._lock:  # Acquire the lock before writing
            self._data[key] = value

    def get(self, key):
        with self._lock:  # Acquire the lock before reading
            return self._data.get(key)

    def remove(self, key):
        with self._lock:  # Acquire the lock before removing
            if key in self._data:
                del self._data[key]

# Example usage of the ThreadSafeDict
def handle_request(username, value):
    shared_dict.set(username, value)  # Update the dictionary
    print(f"Updated {username} to {value}")

# Create an instance of ThreadSafeDict
shared_dict = ThreadSafeDict()

# Simulating multiple threads modifying the dictionary
threads = []

for i in range(10):  # Simulating 10 concurrent requests
    t = threading.Thread(target=handle_request, args=(f'user{i}', i % 2 == 0))
    threads.append(t)
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()

# Print the final state of the shared dictionary
print("Final dictionary state:", shared_dict._data)
