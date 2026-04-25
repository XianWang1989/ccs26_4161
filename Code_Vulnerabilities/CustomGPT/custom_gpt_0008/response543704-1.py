
from flask import Flask, g
import requests

app = Flask(__name__)

# Create a session variable to persist connection
def get_session():
    if 'session' not in g:
        g.session = requests.Session()
    return g.session

def get_xml(f): 
    @wraps(f)
    def wrap(*args, **kwargs):
        # Use the session to get the XML
        session = get_session()
        r = session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')  # Current bottleneck
        data_from_r = r.content  # Process response content as needed
        user = User(data_from_r)  # Create User object
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
