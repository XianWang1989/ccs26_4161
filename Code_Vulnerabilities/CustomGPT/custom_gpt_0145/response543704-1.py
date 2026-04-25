
from flask import Flask
from functools import wraps
import requests

app = Flask(__name__)

# Create a global session object
session = requests.Session()

# Optional: You can set any session-level parameters if needed
# session.headers.update({'User-Agent': 'your-user-agent'})

def get_xml(f):
    @wraps(f)
    def wrap():
        # Use the session to get the XML once
        r = session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')  # Current bottleneck
        if r.status_code == 200:
            user = User(r.content)  # Assuming User can process raw XML content
            response = f(user)
            return response
        else:
            return "Error fetching data", r.status_code
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
