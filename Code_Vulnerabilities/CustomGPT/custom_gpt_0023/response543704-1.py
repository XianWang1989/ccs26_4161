
from flask import Flask
from functools import wraps
import requests

app = Flask(__name__)

# Create a session object that will persist connections
session = requests.Session()

def get_xml(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        # Get the XML before the function call
        r = session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')  # Using the session
        if r.status_code == 200:
            user = User(r.content)  # Assuming User can take raw XML content
            return f(user, *args, **kwargs)
        else:
            return 'Error retrieving data', r.status_code
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
