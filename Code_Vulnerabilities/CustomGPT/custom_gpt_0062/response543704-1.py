
from flask import Flask, g
import requests

app = Flask(__name__)

# Create a requests session to persist connection
def get_session():
    if 'session' not in g:
        g.session = requests.Session()
    return g.session

@app.teardown_appcontext
def teardown_session(exception):
    # Cleanup session
    session = g.pop('session', None)
    if session is not None:
        session.close()

def get_xml(f): 
    def wrap(*args, **kwargs):
        session = get_session()
        r = session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')  # Replace with the actual URL
        user = User(r.content)  # Adjust this based on how the User object is created
        return f(user, *args, **kwargs)
    return wrap

@app.route('/one')
@get_xml
def page_one(user_object):
    return 'some data from user_object: {}'.format(user_object)

@app.route('/two')
@get_xml
def page_two(user_object):
    return 'some other data from user_object: {}'.format(user_object)

if __name__ == '__main__':
    app.run()
