
from flask import Flask
from functools import wraps
import requests

app = Flask(__name__)

# Create a session for persistent connections
session = requests.Session()

def get_xml(f):
    @wraps(f)
    def wrap():
        # Get the XML before each app function
        r = session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')
        if r.status_code == 200:
            user_data = r.content  # Assume XML data is in content
            user = User(user_data)  # Initialize User object with response data
            response = f(user)
            return response
        else:
            return 'Error retrieving data', r.status_code
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
