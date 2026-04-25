
from flask import Flask, g
from functools import wraps
import requests

app = Flask(__name__)

def get_session():
    if 'session' not in g:
        g.session = requests.Session()  # Create a persistent session
    return g.session

def get_xml(f): 
    @wraps(f)
    def wrap(*args, **kwargs):
        session = get_session()  # Use the persistent session
        r = session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')
        r.raise_for_status()  # Raise an error for bad status codes
        user_data = r.text  # Get the XML data
        user = User(user_data)  # Create User object
        response = f(user, *args, **kwargs)
        return response
    return wrap

@app.route('/one')
@get_xml
def page_one(user):
    return 'some data from user: {}'.format(user)

@app.route('/two')
@get_xml
def page_two(user):
    return 'some other data from user: {}'.format(user)

@app.teardown_appcontext
def teardown_session(exception):
    session = g.pop('session', None)
    if session is not None:
        session.close()  # Close the session if it exists

if __name__ == '__main__':
    app.run()
