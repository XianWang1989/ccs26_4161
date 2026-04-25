
from flask import Flask
from functools import wraps
import requests

app = Flask(__name__)

# Create a requests Session object that will persist across requests
session = requests.Session()

def get_xml(f): 
    @wraps(f)
    def wrap():
        # Use the session to get the XML
        r = session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')  # Adjust your URL as needed
        if r.status_code != 200:
            return 'Error retrieving data', 500  # Handle error appropriately
        user = User(r.text)  # Create the User object based on the response
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
