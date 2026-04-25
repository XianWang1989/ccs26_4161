
from flask import Flask
from functools import wraps
import requests

app = Flask(__name__)

# Create a session object to reuse connections
session = requests.Session()

def get_xml(f): 
    @wraps(f)
    def wrap():
        # Get the XML before each app function, using the session
        r = session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')  # Modify URL as needed
        r.raise_for_status()  # Ensure we handle any request errors
        user = User(r.content)  # Assuming User accepts XML content directly
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
