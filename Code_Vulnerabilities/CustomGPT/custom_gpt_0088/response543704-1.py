
from flask import Flask, g
import requests

app = Flask(__name__)

# Create a session globally
@app.before_request
def create_session():
    g.session = requests.Session()

@app.teardown_request
def remove_session(exception=None):
    session = g.pop('session', None)
    if session is not None:
        session.close()

def get_xml(f): 
    @wraps(f)
    def wrap():
        # Use session to perform the request
        r = g.session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')
        if r.status_code == 200:
            user = User(r.content)  # Process the XML response
            response = f(user)
            return response
        else:
            return 'Failed to retrieve data', 500
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
