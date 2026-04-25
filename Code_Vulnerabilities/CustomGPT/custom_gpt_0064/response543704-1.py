
from flask import Flask
from functools import wraps
import requests

app = Flask(__name__)

# Create a session object to persist connections
session = requests.Session()

def get_xml(f): 
    @wraps(f)
    def wrap():
        # Get the XML before each app function
        r = session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')  # Update with the actual URL
        if r.status_code != 200:
            return f"Error: Unable to retrieve data", 500

        user = User(r.content)  # Assuming User is defined elsewhere
        response = f(user)
        return response
    return wrap

@app.route('/one')
@get_xml
def page_one(user_object):
    return f'Some data from user_object: {user_object.some_attribute}'  # Adjust based on User object

@app.route('/two')
@get_xml
def page_two(user_object):
    return f'Some other data from user_object: {user_object.other_attribute}'  # Adjust based on User object

if __name__ == '__main__':
    app.run()
