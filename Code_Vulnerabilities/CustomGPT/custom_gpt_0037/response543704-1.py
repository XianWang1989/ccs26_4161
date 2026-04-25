
from flask import Flask, g
from functools import wraps
import requests

app = Flask(__name__)

# Create a session object that will be used for requests
session = requests.Session()

def get_xml(f): 
    @wraps(f)
    def wrap(*args, **kwargs):
        # Retrieve the user's XML data before each function call
        if 'user_object' not in g:
            r = session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')
            data_from_r = r.text  # Process the response as needed
            g.user_object = User(data_from_r)  # Create User object and store in Flask's global 'g'
        return f(*args, user_object=g.user_object, **kwargs)
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
