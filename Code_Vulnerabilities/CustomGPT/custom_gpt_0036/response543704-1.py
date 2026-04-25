
from flask import Flask, g
from functools import wraps
import requests

app = Flask(__name__)

# Create a requests session to persist connections
session = requests.Session()

# A simple cache to store user data
user_cache = {}

def get_xml(f): 
    @wraps(f)
    def wrap(*args, **kwargs):
        user_id = 'doomcat55'  # Replace this with logic to get the actual user_id if needed
        # Check if the user data is already cached
        if user_id in user_cache:
            user = user_cache[user_id]
        else:
            # Retrieve the XML from myanimelist.net
            r = session.get(f'http://myanimelist.net/malappinfo.php?u={user_id}&status=all&type=anime')
            if r.status_code == 200:
                user = User(r.content)  # Assuming User can be created from raw content
                # Store the user object in the cache
                user_cache[user_id] = user
            else:
                # Handle error appropriately (maybe return an error response)
                return 'Error retrieving data', 500

        # Call the original function with the user object
        response = f(user, *args, **kwargs)
        return response
    return wrap

@app.route('/one')
@get_xml
def page_one(user_object):
    return 'some data from user_object'

@app.route('/two')
@get_xml
def page_two(user_object):
    return 'some other data from user_object'

if __name__ == '__main__':
    app.run()
