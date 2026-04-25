
from flask import Flask, g
import requests

app = Flask(__name__)

# Create a requests session globally
session = requests.Session()

def get_xml(f): 
    @wraps(f)
    def wrap(*args, **kwargs):
        # If user data is not cached, fetch it
        if 'user' not in g:
            r = session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')
            # Here, parse the XML response and create User object
            g.user = User(r.content)  # Replace with actual method to convert XML to User
        response = f(g.user, *args, **kwargs)
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
