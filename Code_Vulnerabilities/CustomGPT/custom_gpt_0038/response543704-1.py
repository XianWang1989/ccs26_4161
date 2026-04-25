
from flask import Flask, g
from functools import wraps
import requests

app = Flask(__name__)

# Create a global session object
session = requests.Session()

def get_xml(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'user' not in g:
            # Only retrieve the XML once per request context
            r = session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')  # Example URL
            user = User(r.content)  # Create User object from the response
            g.user = user  # Store user object in the Flask global context
        return f(g.user, *args, **kwargs)
    return wrap

@app.route('/one')
@get_xml
def page_one(user_object):
    return f'Some data from {user_object}'

@app.route('/two')
@get_xml
def page_two(user_object):
    return f'Some other data from {user_object}'

if __name__ == '__main__':
    app.run()
