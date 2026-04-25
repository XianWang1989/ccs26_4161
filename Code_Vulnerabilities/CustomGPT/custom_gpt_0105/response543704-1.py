
from flask import Flask
from functools import wraps
import requests

app = Flask(__name__)

# Create a session instance
session = requests.Session()

def get_xml(f): 
    @wraps(f)
    def wrap():
        # Get the XML once and reuse the session
        r = session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')
        if r.status_code == 200:
            user = User(r.content)  # Create User object with the XML
            response = f(user)
            return response
        else:
            return 'Error retrieving data', 500
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
