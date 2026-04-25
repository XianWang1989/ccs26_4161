
from flask import Flask
from functools import wraps
import requests

app = Flask(__name__)

# Create a session object to persist connections
session = requests.Session()

def get_xml(f): 
    @wraps(f)
    def wrap():
        # Get the XML before each app function
        response = session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')
        response.raise_for_status()  # Ensure we notice bad responses
        user = User(response.text)  # Assuming you process text here.
        return f(user)
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
