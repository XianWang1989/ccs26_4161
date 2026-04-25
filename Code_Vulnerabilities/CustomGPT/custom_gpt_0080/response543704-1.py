
from flask import Flask
from functools import wraps
import requests

app = Flask(__name__)

# Create a session object
session = requests.Session()

def get_xml(f): 
    @wraps(f)
    def wrap():
        # Use the session to get the XML
        r = session.get('http://myanimelist.net/malappinfo.php?u=your_username&status=all&type=anime')

        if r.status_code == 200:
            user_data = r.text  # XML data
            user = User(user_data)  # Create User object from the data
            response = f(user)
            return response
        else:
            return 'Failed to retrieve data', r.status_code

    return wrap

@app.route('/one')
@get_xml
def page_one(user_object):
    return f'Some data from {user_object}'

@app.route('/two')
@get_xml
def page_two(user_object):
    return f'Some other data from {user_object}'

if __name__ == '__main__':
    app.run()
