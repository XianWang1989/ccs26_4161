
from flask import Flask
from functools import wraps
import requests

app = Flask(__name__)

# Create a session object outside of the route functions
session = requests.Session()

def get_xml(f): 
    @wraps(f)
    def wrap():
        # Use the session to get the XML
        r = session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')  # Update with actual URL
        # Assuming the response is XML
        data_from_r = r.content
        user = User(data_from_r)  # Create User object with fetched data
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
