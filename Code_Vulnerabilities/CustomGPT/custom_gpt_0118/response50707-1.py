
import urllib2
import base64

# Function to make a single authenticated request
def authenticated_request(url, username, passwd):
    # Encode username and password
    b64str = base64.encodestring(f'{username}:{passwd}').strip()

    # Create the request object
    req = urllib2.Request(url)
    # Add the Authorization header
    auth = 'Basic {}'.format(b64str)
    req.add_header('Authorization', auth)

    try:
        # Open the URL
        response = urllib2.urlopen(req)
        # Read and return the response
        return response.read()
    except urllib2.HTTPError as e:
        print(f'HTTP error: {e.code} - {e.reason}')
    except urllib2.URLError as e:
        print(f'URL error: {e.reason}')

# Usage
url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'
response_content = authenticated_request(url, username, passwd)
print(response_content)
