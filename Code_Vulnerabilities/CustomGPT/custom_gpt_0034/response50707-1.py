
import urllib2
import base64

# Define the URL, username, and password
url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Create a Base64 encoded string for the credentials
b64_credentials = base64.b64encode(f'{username}:{passwd}'.encode()).decode()

# Create a request object
req = urllib2.Request(url)

# Add the Authorization header
req.add_header('Authorization', f'Basic {b64_credentials}')

# Make the request
try:
    response = urllib2.urlopen(req)
    # Read and print the response
    print(response.read())
except urllib2.HTTPError as e:
    print(f'HTTPError: {e.code} - {e.reason}')
except urllib2.URLError as e:
    print(f'URLError: {e.reason}')
