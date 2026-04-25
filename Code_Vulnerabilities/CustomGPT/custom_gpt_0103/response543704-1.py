
from flask import Flask
from functools import wraps
import requests

app = Flask(__name__)

# Create a session object
session = requests.Session()

def get_xml(f):
    @wraps(f)
    def wrap():
        # Get the XML using the session to utilize connection pooling
        response = session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')
        if response.status_code == 200:
            data_from_r = response.text  # or response.content depending on your needs
            user = User(data_from_r)  # Create User object from the XML data
            return f(user)
        else:
            return 'Error retrieving data', response.status_code
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
