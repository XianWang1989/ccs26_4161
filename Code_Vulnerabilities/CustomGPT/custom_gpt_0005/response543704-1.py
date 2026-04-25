
from flask import Flask
from functools import wraps
import requests

app = Flask(__name__)

# Create a requests session
session = requests.Session()

def get_xml(f):
    @wraps(f)
    def wrap():
        # Use the persistent session to retrieve XML
        r = session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')
        r.raise_for_status()  # Raise an error for bad responses
        data_from_r = r.text  # Get the XML as text
        user = User(data_from_r)  # Create User object
        response = f(user)
        return response
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
