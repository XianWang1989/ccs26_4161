
import urllib2
import base64

def make_authenticated_request(url, username, password):
    # Create the base64 encoded string for Basic Authentication
    b64str = base64.encodestring(f'{username}:{password}').strip()

    # Create a request object
    req = urllib2.Request(url)

    # Add the Authorization header
    auth = f'Basic {b64str}'
    req.add_header('Authorization', auth)

    try:
        # Open the URL with the request object
        response = urllib2.urlopen(req)
        return response.read()
    except urllib2.HTTPError as e:
        print(f'HTTP error: {e.code} - {e.reason}')
    except urllib2.URLError as e:
        print(f'URL error: {e.reason}')

# Usage example
url = 'http://your-url.com'
username = 'your_username'
password = 'your_password'

response_content = make_authenticated_request(url, username, password)
print(response_content)
