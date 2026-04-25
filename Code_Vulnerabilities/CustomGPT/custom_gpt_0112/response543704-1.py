
from flask import Flask
from functools import wraps
import requests

app = Flask(__name__)

# Create a session object
session = requests.Session()

def get_xml(f):
    @wraps(f)
    def wrap():
        # Use the session to get the XML
        r = session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')
        # Check if the request was successful
        if r.status_code == 200:
            user = User(r.content)  # Create User object with the response content
            response = f(user)
            return response
        else:
            return f"Error retrieving data: {r.status_code}", r.status_code
    return wrap

@app.route('/one')
@get_xml
def page_one(user_object):
    return 'Some data from user_object'

@app.route('/two')
@get_xml
def page_two(user_object):
    return 'Some other data from user_object'

if __name__ == '__main__':
    app.run()
