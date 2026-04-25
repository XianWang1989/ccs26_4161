
from flask import Flask
from functools import wraps
import requests

app = Flask(__name__)

# Create a session object to persist the connection
session = requests.Session()

def get_xml(f): 
    @wraps(f)
    def wrap():
        # Use the session to get XML data
        r = session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime') # Update with actual URL
        r.raise_for_status()  # Raises an error for bad response
        user = User(r.text) # Assuming the User constructor accepts XML as a string
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
