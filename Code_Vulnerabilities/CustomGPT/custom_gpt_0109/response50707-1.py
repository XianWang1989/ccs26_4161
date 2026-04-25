
import urllib2
import base64

# Define the URL and credentials
url = 'http://example.com/protected'
username = 'your_username'
passwd = 'your_password'

# Create the request object
req = urllib2.Request(url)

# Encode the username and password
credentials = f"{username}:{passwd}"
b64_credentials = base64.b64encode(credentials.encode()).decode()
auth_header = f'Basic {b64_credentials}'

# Add the authorization header to the request
req.add_header('Authorization', auth_header)

# Make the request
try:
    response = urllib2.urlopen(req)
    # Read and print the response
    print(response.read())
except urllib2.HTTPError as e:
    print(f"HTTP Error: {e.code} - {e.reason}")
except urllib2.URLError as e:
    print(f"URL Error: {e.reason}")
