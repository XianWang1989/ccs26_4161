
from flask import Flask
from functools import wraps
import requests

app = Flask(__name__)

# Create a session object to persist connections
session = requests.Session()

def get_xml(f): 
    @wraps(f)
    def wrap(*args, **kwargs):
        # Get the XML before each app function
        r = session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')
        r.raise_for_status()  # Raise an error for bad responses
        user = User(r.content)  # Adjust based on how you handle XML
        return f(user, *args, **kwargs)
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
