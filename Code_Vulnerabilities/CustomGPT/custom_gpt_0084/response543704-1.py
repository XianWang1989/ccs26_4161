
from flask import Flask, g
import requests

app = Flask(__name__)

# Create a requests session for persistent connections
session = requests.Session()

# Define a function to get the XML
def get_xml():
    # Fetch the XML only once and store it in the global context
    if 'xml_data' not in g:
        response = session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')
        g.xml_data = response.text  # Store the XML in the Flask context
    return g.xml_data

@app.route('/one')
def page_one():
    xml_data = get_xml()
    user = User(xml_data)  # Process XML to create User object
    return 'Some data from user object'

@app.route('/two')
def page_two():
    xml_data = get_xml()
    user = User(xml_data)  # Process XML to create User object
    return 'Some other data from user object'

if __name__ == '__main__':
    app.run()
