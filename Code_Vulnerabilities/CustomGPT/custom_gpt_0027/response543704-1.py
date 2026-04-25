
from flask import Flask
from functools import wraps
import requests

app = Flask(__name__)

# Create a Session object to persist the connection
session = requests.Session()

def get_xml(f): 
    @wraps(f)
    def wrap(*args, **kwargs):
        # Get the XML before each app function
        r = session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')  # Example endpoint
        user_data = r.text  # Assuming this returns XML data
        user = User(user_data)  # User object creation
        response = f(user, *args, **kwargs)  # Pass user to the view function
        return response
    return wrap

@app.route('/one')
@get_xml
def page_one(user_object):
    return f'some data from {user_object}'

@app.route('/two')
@get_xml
def page_two(user_object):
    return f'some other data from {user_object}'

if __name__ == '__main__':
    app.run()
