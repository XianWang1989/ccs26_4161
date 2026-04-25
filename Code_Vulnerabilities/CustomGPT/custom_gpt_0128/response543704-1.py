
from flask import Flask
from functools import wraps
import requests

app = Flask(__name__)

# Create a session object to persist connections
session = requests.Session()

def get_xml(f): 
    @wraps(f)
    def wrap():
        # Perform the request using the session
        r = session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')
        if r.status_code == 200:
            user = User(r.content)  # Assuming User can process content directly
        else:
            user = None  # Handle error as needed or raise an exception
        response = f(user)
        return response
    return wrap

@app.route('/one')
@get_xml
def page_one(user_object):
    return str(user_object)  # or process user_object to return relevant data

@app.route('/two')
@get_xml
def page_two(user_object):
    return str(user_object)  # or process user_object to return relevant data

if __name__ == '__main__':
    app.run()
