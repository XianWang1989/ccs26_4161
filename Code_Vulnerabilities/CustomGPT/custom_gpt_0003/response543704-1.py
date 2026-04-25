
from flask import Flask
from functools import wraps
import requests

app = Flask(__name__)

# Create a session object that will persist across requests
session = requests.Session()

def get_xml(f): 
    @wraps(f)
    def wrap():
        # Get the XML before each app function
        r = session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')  # Change the URL as necessary
        if r.status_code != 200:
            return 'Failed to retrieve data', 500  # Handle HTTP error

        user = User(data_from_r)  # Assume you've defined User and process r.text or r.content
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
