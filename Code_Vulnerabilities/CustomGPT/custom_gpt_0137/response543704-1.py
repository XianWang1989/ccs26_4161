
from flask import Flask
from functools import wraps
import requests

app = Flask(__name__)

# Create a session object that can be reused for requests
session = requests.Session()

def get_xml(f): 
    @wraps(f)
    def wrap():
        # Use the session to perform the request
        r = session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')  # Replace with appropriate URL
        if r.status_code == 200:
            user = User(r.text)  # Assuming you're passing the XML response text into the User constructor
            response = f(user)
            return response
        else:
            return f"Error fetching data: {r.status_code}", r.status_code
    return wrap

@app.route('/one')
@get_xml
def page_one(user_object):
    # Return some data based on user_object
    return f'Data from user: {user_object.data}'

@app.route('/two')
@get_xml
def page_two(user_object):
    # Return some other data based on user_object
    return f'Other data from user: {user_object.data}'

if __name__ == '__main__':
    app.run()
