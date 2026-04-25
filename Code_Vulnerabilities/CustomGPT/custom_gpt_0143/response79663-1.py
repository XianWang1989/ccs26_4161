
import threading

# Create a dictionary to store user states
user_states = {}
# Create a lock object
lock = threading.Lock()

def update_user_state(username, state):
    with lock:
        user_states[username] = state
        print(f"Updated {username} to {state}")

def get_user_state(username):
    with lock:
        return user_states.get(username, None)

# Example usage
if __name__ == "__main__":
    # Simulate threads updating user states
    threads = []
    for i in range(5):
        username = f"user{i}"
        state = i % 2 == 0  # Alternating states
        thread = threading.Thread(target=update_user_state, args=(username, state))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    # Print final user states
    print("Final user states:", user_states)
