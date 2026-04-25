
from flask import Flask
from functools import wraps
import requests

app = Flask(__name__)

# Create a session object to persist parameters across requests
session = requests.Session()

def get_xml(f): 
    @wraps(f)
    def wrap():
        # Get the XML using the session to reuse the HTTP connection
        r = session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')  # Adjust the URL as needed
        if r.status_code == 200:
            user = User(r.content)  # Assuming that User can accept raw XML string or similar
        else:
            # Handle the error - for example, you can raise an exception or return default values
            user = None  # or raise an exception
        response = f(user)
        return response
    return wrap

@app.route('/one')
@get_xml
def page_one(user_object):
    return 'some data from user_object' if user_object else 'Error retrieving data'

@app.route('/two')
@get_xml
def page_two(user_object):
    return 'some other data from user_object' if user_object else 'Error retrieving data'

if __name__ == '__main__':
    app.run()
