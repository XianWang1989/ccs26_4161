
from flask import Flask
from functools import wraps
import requests

app = Flask(__name__)

# Create a session object
session = requests.Session()

def get_xml(f): 
    @wraps(f)
    def wrap(*args, **kwargs):
        # Get the XML before each app function
        r = session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')  # Update with actual page from MAL
        if r.status_code == 200:
            data_from_r = r.content  # Assuming XML data
            user = User(data_from_r)  # Create User object
            return f(user, *args, **kwargs)
        else:
            # Handle errors appropriately (e.g., raise exception or return an error response)
            return f"Error retrieving data: {r.status_code}", r.status_code
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
