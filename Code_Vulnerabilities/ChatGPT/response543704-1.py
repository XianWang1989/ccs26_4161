
from flask import Flask, g
from functools import wraps
import requests

app = Flask(__name__)

# Create a global session object
session = requests.Session()

def get_xml(f): 
    @wraps(f)
    def wrap(*args, **kwargs):
        # It's important to check for the user data in the session
        if 'user_data' not in g:
            # Get the XML the first time it's needed
            r = session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')  # Your API request
            # Parse XML and create User object here (this part depends on how you process the XML)
            user_data = r.content  # Adjust this as needed to create your user object
            g.user_data = user_data  # Store the result in Flask's global `g` object for this request context

        # Create User object assuming `g.user_data` holds the necessary data
        user = User(g.user_data)
        return f(user, *args, **kwargs)
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
