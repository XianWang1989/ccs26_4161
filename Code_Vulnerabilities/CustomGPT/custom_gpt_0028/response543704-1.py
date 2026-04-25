
from flask import Flask
from functools import wraps
import requests

app = Flask(__name__)

# Initialize a requests session
session = requests.Session()

def get_xml(f): 
    @wraps(f)
    def wrap():
        # Use the session to retrieve the XML
        r = session.get('https://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')
        if r.status_code == 200:
            data_from_r = r.content  # or r.text if you need string
            user = User(data_from_r)  # Create User object with received data
            response = f(user)
            return response
        else:
            return "Error fetching data", 500
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
