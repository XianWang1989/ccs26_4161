
import urllib2
import base64

url = 'http://example.com'  # Replace with your URL
username = 'your_username'   # Replace with your username
passwd = 'your_password'      # Replace with your password

# Encode the username and password
b64str = base64.b64encode(f'{username}:{passwd}'.encode()).decode()

# Create a request object
req = urllib2.Request(url)
# Add the Authorization header
req.add_header('Authorization', 'Basic %s' % b64str)

try:
    # Open the URL
    response = urllib2.urlopen(req)
    # Read the response
    data = response.read()
    print(data)
except urllib2.HTTPError as e:
    print(f'HTTPError: {e.code} - {e.reason}')
except urllib2.URLError as e:
    print(f'URLError: {e.reason}')
