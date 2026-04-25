
from flask import Flask
from functools import wraps
import requests

app = Flask(__name__)

# Create a persistent session
session = requests.Session()

def get_xml(f): 
    @wraps(f)
    def wrap():
        # Get the XML before each app function using the session
        r = session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')  # Current bottleneck
        if r.status_code != 200:
            return 'Error retrieving data', 500
        user = User(r.content)  # Assuming User can take XML content directly
        response = f(user)
        return response
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
