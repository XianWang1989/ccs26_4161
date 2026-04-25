
from flask import Flask
from functools import wraps
import requests

app = Flask(__name__)

# Create a session object to persist connections
session = requests.Session()

def get_xml(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        # Get the XML before each app function
        r = session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')  # Updated URL
        if r.status_code == 200:
            data_from_r = r.text  # XML response as text
            user = User(data_from_r)  # Create User object
            response = f(user, *args, **kwargs)
            return response
        else:
            return "Error retrieving data", 500
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
