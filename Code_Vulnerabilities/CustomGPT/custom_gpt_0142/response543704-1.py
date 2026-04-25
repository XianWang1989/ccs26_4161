
from flask import Flask
from functools import wraps
import requests

app = Flask(__name__)

# Create a session object that will be reused
session = requests.Session()

def get_xml(f): 
    @wraps(f)
    def wrap(*args, **kwargs):
        # Get the XML before each app function
        r = session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')  # Adjust URL accordingly
        data_from_r = r.content  # Assuming the XML content is in the response body
        user = User(data_from_r)  # User object
        response = f(user, *args, **kwargs)  # Pass user_object to the wrapped function
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
