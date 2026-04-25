
from flask import Flask
from functools import wraps
import requests

app = Flask(__name__)

# Create a session for persistent connections
session = requests.Session()

def get_xml(f): 
    @wraps(f)
    def wrap():
        # Get the XML before each app function using the session
        r = session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')  # Current bottleneck
        if r.status_code == 200:
            user = User(r.content)  # Adjust this as necessary for your User object
            response = f(user)
            return response
        else:
            return 'Error fetching data', r.status_code
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
