
from flask import Flask
from functools import wraps
import requests

app = Flask(__name__)

# Create a global session object
session = requests.Session()

def get_xml(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        # Perform the GET request using the session
        r = session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')  # Example URL
        if r.status_code == 200:
            user = User(r.content)  # Initialize User object with the response content
            return f(user, *args, **kwargs)
        else:
            return 'Error fetching data', r.status_code
    return wrap

@app.route('/one')
@get_xml
def page_one(user):
    return 'Some data from user: {}'.format(user.some_attribute)

@app.route('/two')
@get_xml
def page_two(user):
    return 'Some other data from user: {}'.format(user.some_other_attribute)

if __name__ == '__main__':
    app.run()
