
import urllib2
import base64

# Specify your URL and credentials
url = 'http://example.com'
username = 'your_username'
passwd = 'your_password'

# Create a base64 encoded string of the username and password
b64str = base64.b64encode(f'{username}:{passwd}'.encode()).decode()

# Create the request object
req = urllib2.Request(url)

# Add the Authorization header
req.add_header('Authorization', 'Basic ' + b64str)

# Send the request and read the response
try:
    response = urllib2.urlopen(req)
    content = response.read()
    print(content)
except urllib2.HTTPError as e:
    print(f'HTTPError: {e.code}')
except urllib2.URLError as e:
    print(f'URLError: {e.reason}')
