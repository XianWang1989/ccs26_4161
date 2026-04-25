
from flask import Flask
from functools import wraps
import requests

app = Flask(__name__)

# Create a global session for reusing connections
session = requests.Session()

def get_xml(f): 
    @wraps(f)
    def wrap():
        # Use the session to make the request
        r = session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')

        if r.status_code == 200:
            data_from_r = r.text  # Assuming you want the response as XML
            user = User(data_from_r)  # Create the User object
            response = f(user)
            return response
        else:
            return "Error retrieving data", r.status_code

    return wrap

@app.route('/one')
@get_xml
def page_one(user_object):
    return f'User data for page one: {user_object.data}'

@app.route('/two')
@get_xml
def page_two(user_object):
    return f'User data for page two: {user_object.data}'

if __name__ == '__main__':
    app.run()
