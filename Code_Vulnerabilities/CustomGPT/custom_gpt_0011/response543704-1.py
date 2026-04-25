
from flask import Flask
from functools import wraps
import requests

app = Flask(__name__)

# Create a session object that can be used to persist a connection
session = requests.Session()

def get_xml(f): 
    @wraps(f)
    def wrap():
        # Get the XML before each app function using the session
        r = session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')  # Current bottleneck
        if r.status_code == 200:
            user = User(r.content)  # Process the response
        else:
            user = None  # Handle the error case as needed

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
