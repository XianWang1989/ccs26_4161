
from flask import Flask
from functools import wraps
import requests

app = Flask(__name__)

# Create a session for persistent connections
session = requests.Session()

def get_xml(f): 
    @wraps(f)
    def wrap():
        # Get the XML before each app function
        response = session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')  # Updated URL
        if response.status_code == 200:
            user = User(response.content)  # Process your XML here
            return f(user)
        else:
            return "Error retrieving data", 500  # Handle errors appropriately
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
