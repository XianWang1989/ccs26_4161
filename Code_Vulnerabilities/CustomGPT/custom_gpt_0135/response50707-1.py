
import urllib2
import base64

# URL and credentials
url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Encode the credentials
credentials = f"{username}:{passwd}"
b64_credentials = base64.b64encode(credentials.encode()).decode()

# Create the request object
req = urllib2.Request(url)

# Add the Authorization header with the encoded credentials
req.add_header('Authorization', f'Basic {b64_credentials}')

# Make the request
try:
    response = urllib2.urlopen(req)
    print(response.read())
except urllib2.HTTPError as e:
    print(f'HTTP error: {e.code} - {e.reason}')
except urllib2.URLError as e:
    print(f'URL error: {e.reason}')
