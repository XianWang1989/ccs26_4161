
from flask import Flask, g
from functools import wraps
import requests

app = Flask(__name__)

# Create a requests session
session = requests.Session()

def get_xml(f): 
    @wraps(f)
    def wrap(*args, **kwargs):
        # Store the user object in Flask's global context
        if 'user_object' not in g:
            # Make the request only if user_object is not cached in `g`
            r = session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')
            user_data = r.text  # Assuming the response is XML or similar
            g.user_object = User(user_data)  # Create User object

        response = f(g.user_object, *args, **kwargs)
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
