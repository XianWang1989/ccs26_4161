
from flask import Flask
from functools import wraps
import requests

app = Flask(__name__)

# Create a persistent session
session = requests.Session()

def get_xml(f): 
    @wraps(f)
    def wrap():
        # Get the XML only once for each request
        r = session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')  # Current bottleneck
        # Validate response status
        r.raise_for_status()  
        user = User(r.text)  # Parse XML and create User object
        response = f(user)
        return response
    return wrap

@app.route('/one')
@get_xml
def page_one(user_object):
    return 'some data from user_object: {}'.format(user_object.data)

@app.route('/two')
@get_xml
def page_two(user_object):
    return 'some other data from user_object: {}'.format(user_object.data)

if __name__ == '__main__':
    app.run()
