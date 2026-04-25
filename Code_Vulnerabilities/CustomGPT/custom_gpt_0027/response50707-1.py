
import urllib2
import base64

# Function to make a single request with authentication
def make_authenticated_request(url, username, password):
    # Base64 encode the username and password
    b64_credentials = base64.b64encode(f'{username}:{password}'.encode()).decode()

    # Create a request object
    req = urllib2.Request(url)
    # Add the Authorization header
    req.add_header('Authorization', 'Basic ' + b64_credentials)

    try:
        # Open the URL
        response = urllib2.urlopen(req)
        # Read and return the response
        return response.read()
    except urllib2.HTTPError as e:
        print(f'HTTPError: {e.code} - {e.reason}')
    except urllib2.URLError as e:
        print(f'URLError: {e.reason}')

# Usage
url = 'http://example.com/protected'
username = 'jpx'
password = 'jpx123'
content = make_authenticated_request(url, username, password)

if content:
    print(content)
