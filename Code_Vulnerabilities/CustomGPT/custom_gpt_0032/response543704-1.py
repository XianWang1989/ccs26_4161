
from flask import Flask
from functools import wraps
import requests

app = Flask(__name__)

# Create a session object to persist connections
session = requests.Session()

def get_xml(f): 
    @wraps(f)
    def wrap(*args, **kwargs):
        # Use the session to get the XML once and reuse it for subsequent requests
        r = session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')
        if r.status_code == 200:
            user_data = r.content  # Assuming XML content is in r.content
            user = User(user_data)  # Create a User object from the response
            response = f(user, *args, **kwargs)  # Pass user object to the view function
            return response
        else:
            return 'Error fetching data', r.status_code
    return wrap


@app.route('/one')
@get_xml
def page_one(user_object):
    return 'Some data from user_object: {}'.format(user_object.some_attribute)


@app.route('/two')
@get_xml
def page_two(user_object):
    return 'Some other data from user_object: {}'.format(user_object.some_other_attribute)

if __name__ == '__main__':
    app.run()
