
from flask import Flask
from functools import wraps
import requests

app = Flask(__name__)

# Create a session once and use it in requests
session = requests.Session()

def get_xml(f): 
    @wraps(f)
    def wrap():
        # Get the XML before each app function
        r = session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')  # Using the existing session
        if r.status_code == 200:
            user = User(r.text)  # Assuming User can accept the XML data as text
        else:
            user = None  # Handle error as necessary
        response = f(user) if user else "Failed to retrieve data"
        return response
    return wrap

@app.route('/one')
@get_xml
def page_one(user_object):
    return f'Some data from user_object: {user_object}'

@app.route('/two')
@get_xml
def page_two(user_object):
    return f'Some other data from user_object: {user_object}'

if __name__ == '__main__':
    app.run()
