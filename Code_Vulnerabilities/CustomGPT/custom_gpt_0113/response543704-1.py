
from flask import Flask
from functools import wraps
import requests

app = Flask(__name__)

# Create a global session instance
session = requests.Session()

def get_xml(f): 
    @wraps(f)
    def wrap():
        # Get the XML before each app function using the persistent session
        r = session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')  # Adjust URL as necessary
        if r.status_code != 200:
            # Handle error cases appropriately
            return 'Error fetching data', 500
        data_from_r = r.text  # or r.json() based on your API response
        user = User(data_from_r)  # User object created from XML
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
