
import threading

# Shared dictionary for user states
user_states = {}
# Lock to ensure thread safety
lock = threading.Lock()

def update_user_state(username, state):
    """Update the user state in a thread-safe way."""
    with lock:
        user_states[username] = state

def get_user_state(username):
    """Retrieve the user state in a thread-safe way."""
    with lock:
        return user_states.get(username, None)

# Example usage in a simulated request handler
def handle_request(username, state):
    # Update user state
    update_user_state(username, state)
    # Retrieve the updated state
    return get_user_state(username)

# Simulated multithreaded requests
def simulate_requests():
    handle_request('user1', True)
    print(handle_request('user1', False))

# Start multiple threads to simulate concurrent access
threads = []
for i in range(10):
    t = threading.Thread(target=simulate_requests)
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

# Check final states
print(user_states)
