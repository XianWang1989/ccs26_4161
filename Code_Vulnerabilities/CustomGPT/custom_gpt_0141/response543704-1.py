
from flask import Flask, g
from functools import wraps
import requests

app = Flask(__name__)

# Create a global session object
session = requests.Session()

def get_xml(f): 
    @wraps(f)
    def wrap(*args, **kwargs):
        # Use the global session to get the XML
        r = session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')  # Current bottleneck
        if r.status_code == 200:
            data_from_r = r.text  # Get the XML data
            user = User(data_from_r)  # Assuming User is your model for processing data
            response = f(user, *args, **kwargs)
            return response
        else:
            return "Error retrieving data", r.status_code
    return wrap

@app.route('/one')
@get_xml
def page_one(user_object):
    # Process user_object and return data
    return f'Some data from {user_object.username}'  # Example of accessing user data

@app.route('/two')
@get_xml
def page_two(user_object):
    # Process user_object and return different data
    return f'Some other data from {user_object.username}'  # Example of accessing user data

if __name__ == '__main__':
    app.run()
