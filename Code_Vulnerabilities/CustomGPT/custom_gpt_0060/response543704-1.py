
from flask import Flask
from functools import wraps
import requests

app = Flask(__name__)

# Create a global requests session
session = requests.Session()

def get_xml(f):
    @wraps(f)
    def wrap():
        # Use the global session to get the XML before each app function
        r = session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')
        if r.status_code == 200:
            data_from_r = r.content  # Or r.text if you need it as a string
            user = User(data_from_r)  # Assuming User takes the raw XML
            response = f(user)
            return response
        else:
            # Handle error, e.g., return a default response or raise an exception
            return "Error retrieving data", 500
    return wrap

@app.route('/one')
@get_xml
def page_one(user_object):
    return f'Some data from user_object: {user_object.some_attribute}'

@app.route('/two')
@get_xml
def page_two(user_object):
    return f'Some other data from user_object: {user_object.some_attribute}'

if __name__ == '__main__':
    app.run()
