
from flask import Flask, g
from functools import wraps
import requests

app = Flask(__name__)

# Create a session as a global object for the Flask app
@app.before_request
def before_request():
    g.session = requests.Session()

def get_xml(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        # Use the session to get the XML
        r = g.session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')
        if r.status_code == 200:
            user = User(r.content)  # Assuming User can accept XML data directly
            return f(user, *args, **kwargs)
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
