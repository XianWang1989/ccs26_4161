
from flask import Flask
from functools import wraps
import requests

app = Flask(__name__)

# Create a session
session = requests.Session()

def get_xml(f): 
    @wraps(f)
    def wrap():
        # Get the XML once per request
        r = session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')
        # Make sure to check if the request was successful
        if r.status_code == 200:
            user = User(r.content)  # Create User object with response content
        else:
            user = None  # Handle error appropriately here
        response = f(user)
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
