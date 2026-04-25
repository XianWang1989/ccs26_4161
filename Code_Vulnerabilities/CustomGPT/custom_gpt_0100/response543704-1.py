
from flask import Flask, g
from functools import wraps
import requests

app = Flask(__name__)

# Create a session as a global object
def get_session():
    if 'session' not in g:
        g.session = requests.Session()
    return g.session

def get_xml(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        session = get_session()
        # Make the request using the session
        r = session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')
        user = User(r.content)  # Process the response content to create a User object
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

@app.teardown_appcontext
def close_session(exception):
    session = g.pop('session', None)
    if session is not None:
        session.close()

if __name__ == '__main__':
    app.run()
