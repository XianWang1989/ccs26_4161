
import urllib2
import base64

# Define the URL, username, and password
url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Manually encode the credentials
credentials = f"{username}:{passwd}"
b64_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

# Create a request object
req = urllib2.Request(url)
# Add the Authorization header
req.add_header('Authorization', f'Basic {b64_credentials}')

try:
    # Open the URL with the request
    response = urllib2.urlopen(req)
    print(response.read())
except urllib2.HTTPError as e:
    print(f"HTTPError: {e.code} - {e.reason}")
except urllib2.URLError as e:
    print(f"URLError: {e.reason}")
