
from flask import Flask
from functools import wraps
import requests

app = Flask(__name__)

# Create a Session object
session = requests.Session()

def get_xml(f): 
    @wraps(f)
    def wrap():
        # Use the session to send a GET request
        r = session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')  # Update the URL as needed
        r.raise_for_status()  # Check for request errors
        user = User(r.content)  # Create User object with the response data
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
