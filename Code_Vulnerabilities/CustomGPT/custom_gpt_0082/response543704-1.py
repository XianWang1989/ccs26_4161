
from flask import Flask
from functools import wraps
import requests

app = Flask(__name__)

# Create a session object for persistent connections
session = requests.Session()

def get_xml(f): 
    @wraps(f)
    def wrap():
        # Get the XML using the persistent session
        r = session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')
        if r.status_code == 200:
            user = User(r.content)  # Process the data here
        else:
            user = None  # Handle error
        response = f(user)
        return response
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
