
from flask import Flask
from functools import wraps
import requests

app = Flask(__name__)

# Create a requests Session
session = requests.Session()

# Decorator to get XML data once and reuse it
def get_xml(f): 
    @wraps(f)
    def wrap():
        # Retrieve the XML once
        if not hasattr(wrap, 'user'):
            r = session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')
            if r.status_code == 200:
                data_from_r = r.content  # Use r.text for string or r.content for bytes
                wrap.user = User(data_from_r)  # Create User object once
            else:
                wrap.user = None  # Handle the error as necessary
        response = f(wrap.user)
        return response
    return wrap

@app.route('/one')
@get_xml
def page_one(user_object):
    if user_object:
        return f'Some data from user object: {user_object.some_property}'
    return 'Failed to retrieve user data.'

@app.route('/two')
@get_xml
def page_two(user_object):
    if user_object:
        return f'Some other data from user object: {user_object.other_property}'
    return 'Failed to retrieve user data.'

if __name__ == '__main__':
    app.run()
