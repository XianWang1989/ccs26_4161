
from flask import Flask, g
from functools import wraps
import requests

app = Flask(__name__)

# Create a global session object
session = requests.Session()

def get_xml(f): 
    @wraps(f)
    def wrap(*args, **kwargs):
        # Use the global session to retrieve the XML
        r = session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')  # Example URL
        if r.status_code == 200:
            user = User(r.content)  # Assuming User can handle XML content directly
            return f(user, *args, **kwargs)
        else:
            return 'Error retrieving data', 500
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
