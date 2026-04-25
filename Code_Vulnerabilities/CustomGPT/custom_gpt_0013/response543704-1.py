
from flask import Flask
from functools import wraps
import requests

app = Flask(__name__)

# Create a session object that will persist between requests
session = requests.Session()

def get_xml(f): 
    @wraps(f)
    def wrap():
        # Get the XML before each app function, using the session
        r = session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')  # Adjust the URL as needed
        if r.status_code == 200:
            # Assuming the XML data can be processed here
            user = User(r.content)  # Process the XML directly from response content
            response = f(user)
            return response
        else:
            return "Error fetching data", r.status_code
    return wrap

@app.route('/one')
@get_xml
def page_one(user_object):
    return f'Some data from user: {user_object}'

@app.route('/two')
@get_xml
def page_two(user_object):
    return f'Some other data from user: {user_object}'

if __name__ == '__main__':
    app.run()
