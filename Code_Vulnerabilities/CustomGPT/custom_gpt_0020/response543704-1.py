
from flask import Flask
from functools import wraps
import requests

app = Flask(__name__)

# Create a session object that will be used to persist the connection
session = requests.Session()

def get_xml(f): 
    @wraps(f)
    def wrap():
        # Make a request using the session, which persists the connection
        r = session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime') # Use the appropriate URL
        if r.status_code == 200:
            user = User(r.content)  # Assuming you are getting valid XML content from the response
            response = f(user)
            return response
        else:
            return f"Error fetching data: {r.status_code}", r.status_code
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
