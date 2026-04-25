
from flask import Flask, g
from functools import wraps
import requests

app = Flask(__name__)

# Create a global session object
session = requests.Session()

def get_xml(f): 
    @wraps(f)
    def wrap():
        # Use the session to make a request to the API
        r = session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')
        r.raise_for_status()  # Ensure we handle HTTP errors
        user = User(r.content)  # Process the XML content to create a User object
        response = f(user)
        return response
    return wrap

@app.route('/one')
@get_xml
def page_one(user_object):
    return f'Some data from user: {user_object}'

@app.route('/two')
@get_xml
def page_two(user_object):
    return f'Some other data from user: {user_object}'

if __name__ == '__main__':
    app.run()
