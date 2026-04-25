
from flask import Flask
from functools import wraps
import requests

app = Flask(__name__)

# Create a session object for persistent connections
session = requests.Session()

def get_xml(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        # Get the XML before each app function
        r = session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')

        # Check if the request was successful
        r.raise_for_status()

        # Process the XML response to create a User object
        user = User(r.text)  # Assuming User can handle XML directly.
        response = f(user, *args, **kwargs)
        return response
    return wrap

@app.route('/one')
@get_xml
def page_one(user_object):
    return 'some data from user_object: {}'.format(user_object.some_data)

@app.route('/two')
@get_xml
def page_two(user_object):
    return 'some other data from user_object: {}'.format(user_object.some_other_data)

if __name__ == '__main__':
    app.run()
