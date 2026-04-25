
from flask import Flask, g
from functools import wraps
import requests

app = Flask(__name__)

# Create a session for persistent connections
def get_session():
    if 'session' not in g:
        g.session = requests.Session()
    return g.session

def get_xml(f): 
    @wraps(f)
    def wrap(*args, **kwargs):
        session = get_session()
        r = session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')  # Replace with relevant URL
        user = User(r.content)  # Create User object based on response
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

@app.teardown_appcontext
def teardown_session(exception):
    session = g.pop('session', None)
    if session is not None:
        session.close()

if __name__ == '__main__':
    app.run()
