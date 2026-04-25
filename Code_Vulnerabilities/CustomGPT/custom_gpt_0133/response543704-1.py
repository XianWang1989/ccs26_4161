
from flask import Flask, g
from functools import wraps
import requests

app = Flask(__name__)

# Create a requests session
session = requests.Session()

def get_xml(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        # Get the XML before each app function
        response = session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')
        if response.status_code != 200:
            return "Error: Could not retrieve data", 500

        # You will need to parse the XML here and create a User object with the data
        user_data = response.text  # This is where you'll parse the XML
        user = User(user_data)  # Create the User object
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
