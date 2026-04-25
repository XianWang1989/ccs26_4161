
# Not thread-safe
user_status = {}

def update_status(username, status):
    user_status[username] = status
