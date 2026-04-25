
import urllib2
import base64

url = 'http://yoururl.com'
username = 'your_username'
passwd = 'your_password'

# Create a request object
req = urllib2.Request(url)

# Encode the username and password
credentials = f"{username}:{passwd}"
b64_credentials = base64.b64encode(credentials.encode()).decode()

# Set the Authorization header
auth_header = f"Basic {b64_credentials}"
req.add_header('Authorization', auth_header)

try:
    # Send the request
    response = urllib2.urlopen(req)
    print(response.read())
except urllib2.HTTPError as e:
    print(f"HTTP Error: {e.code} - {e.reason}")
except urllib2.URLError as e:
    print(f"URL Error: {e.reason}")
