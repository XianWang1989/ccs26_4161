
import urllib2
import base64

def request_with_basic_auth(url, username, password):
    # Create a base64 encoded string
    credentials = f'{username}:{password}'
    b64_credentials = base64.b64encode(credentials.encode()).decode()

    # Create a request with the Authorization header
    req = urllib2.Request(url)
    req.add_header('Authorization', f'Basic {b64_credentials}')

    try:
        response = urllib2.urlopen(req)
        print(response.read())
    except urllib2.HTTPError as e:
        print(f'HTTPError: {e.code} - {e.reason}')
    except urllib2.URLError as e:
        print(f'URLError: {e.reason}')

# Usage
url = 'http://example.com'  # Replace with your URL
username = 'jpx'
password = 'jpx123'

request_with_basic_auth(url, username, password)
