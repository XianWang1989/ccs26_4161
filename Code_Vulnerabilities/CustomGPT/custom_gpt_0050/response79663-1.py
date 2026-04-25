
import threading

# Create a dictionary to hold user states
user_states = {}
# Create a lock object
lock = threading.Lock()

def update_user_state(username, state):
    with lock:  # Acquire the lock
        user_states[username] = state  # Update the dictionary safely

def get_user_state(username):
    with lock:  # Acquire the lock
        return user_states.get(username, None)  # Safely retrieve the state

# Example usage in a thread
def handle_request(username, new_state):
    update_user_state(username, new_state)
    state = get_user_state(username)
    print(f"User: {username}, State: {state}")

# Example of starting threads
threads = []
for i in range(10):  # Simulate 10 requests
    t = threading.Thread(target=handle_request, args=(f'user{i}', True))
    threads.append(t)
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()
