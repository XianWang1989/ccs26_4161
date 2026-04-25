
from flask import Flask, jsonify
from functools import wraps
import requests
import time

app = Flask(__name__)

# Simulate shared state for the XML data and last fetched time
xml_data = None
last_fetched = 0
fetch_interval = 3600  # 1 hour

def fetch_xml():
    global xml_data, last_fetched

    # Check if we need to refresh the data
    if time.time() - last_fetched > fetch_interval:
        r = requests.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')
        xml_data = r.text  # Store the XML data
        last_fetched = time.time()
    return xml_data

def get_xml(f): 
    @wraps(f)
    def wrap():
        data = fetch_xml()  # Fetch or reuse the XML data
        user = User(data)  # User object
        response = f(user)
        return response
    return wrap

@app.route('/one')
@get_xml
def page_one(user_object):
    return jsonify({'data': 'some data from user_object'})

@app.route('/two')
@get_xml
def page_two(user_object):
    return jsonify({'data': 'some other data from user_object'})

if __name__ == '__main__':
    app.run()
