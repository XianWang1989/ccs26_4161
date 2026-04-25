
from flask import Flask
from functools import wraps
import requests

app = Flask(__name__)

# Create a session outside of the decorator to persist it
session = requests.Session()

def get_xml(f): 
    @wraps(f)
    def wrap(*args, **kwargs):
        # Use the session to make the request
        r = session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')
        if r.status_code != 200:
            return 'Error fetching data', 500

        user = User(r.content)  # Adjust based on your User constructor
        response = f(user, *args, **kwargs)
        return response
    return wrap

@app.route('/one')
@get_xml
def page_one(user_object):
    return 'Data from user_object for page one: {}'.format(user_object)

@app.route('/two')
@get_xml
def page_two(user_object):
    return 'Data from user_object for page two: {}'.format(user_object)

if __name__ == '__main__':
    app.run()
