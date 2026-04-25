from flask import Flask
from functools import wraps
import requests

app = Flask(__name__)

# Create a session object at the global level
session = requests.Session()

def get_xml(f): 
    @wraps(f)
    def wrap():
        # Use the persistent session to get the XML
        r = session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')  # Use the session here
        if r.status_code == 200:
            user = User(r.text)  # Assuming you have a User object that processes the XML
            response = f(user)
            return response
        else:
            return 'Error fetching data', 500
    return wrap


@app.route('/one')
@get_xml
def page_one(user_object):
    # Process and return some data from the user_object
    return f'Some data from user_object: {user_object.some_data()}'

@app.route('/two')
@get_xml
def page_two(user_object):
    # Process and return other data from the user_object
    return f'Other data from user_object: {user_object.other_data()}'

if __name__ == '__main__':
    app.run(debug=True)
