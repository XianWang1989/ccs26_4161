
import urllib2
import base64

# Function to create a request with basic authentication
def make_authenticated_request(url, username, password):
    # Create a request object
    req = urllib2.Request(url)

    # Encode the username and password into base64
    b64_auth = base64.encodestring(f'{username}:{password}').strip()

    # Add the Authorization header
    req.add_header('Authorization', f'Basic {b64_auth}')

    try:
        # Open the URL with the authenticated request
        response = urllib2.urlopen(req)
        return response.read()
    except urllib2.HTTPError as e:
        print(f'HTTP Error: {e.code} - {e.reason}')
    except urllib2.URLError as e:
        print(f'Failed to reach server: {e.reason}')

# Example usage
if __name__ == '__main__':
    url = 'http://xxxx'
    username = 'jpx'
    password = 'jpx123'
    result = make_authenticated_request(url, username, password)
    if result:
        print(result)
