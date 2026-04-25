
import threading

# Create a Lock object
lock = threading.Lock()

# Dictionary to store user data
user_status = {}

def update_user_status(username, status):
    # Acquire the lock before modifying the dictionary
    with lock:
        user_status[username] = status

        # Optionally, print the updated dictionary for debugging
        print(f"Updated user status: {username} -> {status}")

def get_user_status(username):
    # Acquire the lock before reading from the dictionary
    with lock:
        return user_status.get(username, False)  # Return False if username not found

# Example usage
def handle_request(username, status):
    update_user_status(username, status)
    print(f"Status for {username}: {get_user_status(username)}")

# Simulating multiple threads updating the dictionary
if __name__ == '__main__':
    threading.Thread(target=handle_request, args=("user1", True)).start()
    threading.Thread(target=handle_request, args=("user2", False)).start()
    threading.Thread(target=handle_request, args=("user1", False)).start()
