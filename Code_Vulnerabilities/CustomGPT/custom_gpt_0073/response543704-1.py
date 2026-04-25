
from flask import Flask
from functools import wraps
import requests

app = Flask(__name__)

# Create a session that will persist across requests
session = requests.Session()

def get_xml(f): 
    @wraps(f)
    def wrap(*args, **kwargs):
        # Get the XML before each app function
        r = session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')  # Current bottleneck
        r.raise_for_status()  # Raise an error for bad responses
        user = User(r.content)  # Assuming User class processes XML content
        response = f(user, *args, **kwargs)
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
