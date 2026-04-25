
import urllib2
import base64

# Define your URL and credentials
url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Create the base64 string for the credentials
credentials = f'{username}:{passwd}'
b64_credentials = base64.b64encode(credentials.encode()).decode()

# Create a request object
req = urllib2.Request(url)

# Add the Authorization header
auth_header = f'Basic {b64_credentials}'
req.add_header('Authorization', auth_header)

try:
    # Open the URL
    response = urllib2.urlopen(req)
    print(response.read())  # Print the response content
except urllib2.HTTPError as e:
    print(f'HTTP error: {e.code} {e.reason}')
except urllib2.URLError as e:
    print(f'Failed to reach the server: {e.reason}')
