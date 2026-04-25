
import urllib2
import base64

# Define the URL and credentials
url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Encode username and password in Base64
credentials = f"{username}:{passwd}"
b64_credentials = base64.b64encode(credentials.encode()).decode()

# Create a request and set the Authorization header
req = urllib2.Request(url)
req.add_header('Authorization', 'Basic ' + b64_credentials)

# Make the request
try:
    response = urllib2.urlopen(req)
    print(response.read())
except urllib2.HTTPError as e:
    print(f"HTTP Error: {e.code} - {e.reason}")
except urllib2.URLError as e:
    print(f"Failed to reach the server: {e.reason}")
