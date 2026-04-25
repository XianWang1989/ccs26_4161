
from flask import Flask
from functools import wraps
import requests

app = Flask(__name__)

# Create a Session object to persist connections
session = requests.Session()

def fetch_user_data():
    # This function handles the retrieval of XML data from the API
    response = session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')
    response.raise_for_status()  # Raise an error for bad responses
    return response.content  # Return the XML data as content

def get_xml(f): 
    @wraps(f)
    def wrap():
        xml_data = fetch_user_data()  # Fetch the XML data using the persistent session
        user = User(xml_data)  # Process the XML data into a User object
        response = f(user)
        return response
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
