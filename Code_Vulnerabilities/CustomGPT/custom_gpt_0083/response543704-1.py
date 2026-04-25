
from flask import Flask
from functools import wraps
import requests

app = Flask(__name__)

# Create a global session object to be reused
session = requests.Session()

def get_xml(f):
    @wraps(f)
    def wrap():
        # Use the session to get the XML from myanimelist.net
        r = session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')  # Adjust URL as needed
        if r.status_code == 200:
            data_from_r = r.text  # or r.content if you need raw bytes
            user = User(data_from_r)  # Create your User object
            response = f(user)
            return response
        else:
            return 'Error fetching data', r.status_code
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
