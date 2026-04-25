
from flask import Flask
from functools import wraps
import requests

app = Flask(__name__)

# Create a session object
session = requests.Session()

def get_xml(f):
    @wraps(f)
    def wrap():
        # Get the XML before each app function
        response = session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')
        if response.ok:
            user = User(response.text)  # Create User object from response
        else:
            user = None  # Handle error or default user object

        return f(user)
    return wrap

@app.route('/one')
@get_xml
def page_one(user_object):
    return f'Some data from user_object: {user_object}'

@app.route('/two')
@get_xml
def page_two(user_object):
    return f'Some other data from user_object: {user_object}'

if __name__ == '__main__':
    app.run()
