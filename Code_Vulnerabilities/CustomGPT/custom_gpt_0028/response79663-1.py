
import threading

class ThreadSafeDictionary:
    def __init__(self):
        self.lock = threading.Lock()
        self.data = {}

    def set_value(self, username, value):
        with self.lock:
            self.data[username] = value

    def get_value(self, username):
        with self.lock:
            return self.data.get(username, None)

# Example usage
if __name__ == "__main__":
    thread_safe_dict = ThreadSafeDictionary()

    def thread_function(username):
        thread_safe_dict.set_value(username, True)
        print(f"{username}: {thread_safe_dict.get_value(username)}")

    # Creating multiple threads
    threads = []
    for i in range(20):
        username = f"user_{i}"
        thread = threading.Thread(target=thread_function, args=(username,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()
