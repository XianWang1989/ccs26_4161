
import urllib2
import base64

# Define the URL and credentials
url = 'http://example.com/protected'
username = 'jpx'
passwd = 'jpx123'

# Encode the username and password
credentials = f'{username}:{passwd}'
b64_credentials = base64.b64encode(credentials.encode()).decode()

# Create the request with the Authorization header
req = urllib2.Request(url)
req.add_header('Authorization', f'Basic {b64_credentials}')

# Perform the request and handle the response
try:
    response = urllib2.urlopen(req)
    content = response.read()  # Read the response content
    print(content)  # Print the response
except urllib2.HTTPError as e:
    print(f'HTTP Error: {e.code} - {e.reason}')
except urllib2.URLError as e:
    print(f'URL Error: {e.reason}')
