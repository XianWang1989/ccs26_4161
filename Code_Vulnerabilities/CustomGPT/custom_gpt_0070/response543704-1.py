
from flask import Flask, g
from functools import wraps
import requests

app = Flask(__name__)

# Create a session object to persist the connection
session = requests.Session()

def get_xml(f): 
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'user_object' not in g:  # Check if user object is already created
            # Get the XML if not already done
            r = session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')
            if r.status_code == 200:
                user_data = r.content  # Process the XML data
                g.user_object = User(user_data)  # Create User object
            else:
                g.user_object = None
        return f(g.user_object, *args, **kwargs)
    return wrap

@app.route('/one')
@get_xml
def page_one(user_object):
    if user_object:
        return f'Some data from {user_object}'
    return 'User not found.'

@app.route('/two')
@get_xml
def page_two(user_object):
    if user_object:
        return f'Some other data from {user_object}'
    return 'User not found.'

if __name__ == '__main__':
    app.run()
