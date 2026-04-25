
from flask import Flask
from functools import wraps
import requests

app = Flask(__name__)

# Create a session object to persist the connection
session = requests.Session()

def get_xml(f):
    @wraps(f)
    def wrap():
        # Use the session to get the XML
        r = session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')  # Replace with actual URL
        if r.status_code != 200:
            return 'Error retrieving data', 500  # Handle connection error
        data_from_r = r.text  # Assuming the response is XML
        user = User(data_from_r)  # Create user object from XML
        response = f(user)
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
