
import threading

# Initialize a lock
lock = threading.Lock()

# Dictionary to hold username and Boolean values
user_dict = {}

def update_user_status(username, status):
    with lock:  # Acquire lock before updating the dictionary
        user_dict[username] = status

# Example usage
thread1 = threading.Thread(target=update_user_status, args=('user1', True))
thread2 = threading.Thread(target=update_user_status, args=('user2', False))

thread1.start()
thread2.start()
thread1.join()
thread2.join()

print(user_dict)
