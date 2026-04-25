
import urllib2
import base64

# Define the URL and credentials
url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Create the base64 encoded credentials
credentials = f'{username}:{passwd}'
b64_credentials = base64.b64encode(credentials.encode()).decode()

# Create a request and add the Authorization header
req = urllib2.Request(url)
req.add_header('Authorization', 'Basic ' + b64_credentials)

# Make the request
try:
    response = urllib2.urlopen(req)
    # Read and print the response
    print(response.read())
except urllib2.HTTPError as e:
    print(f'HTTPError: {e.code} - {e.reason}')
except urllib2.URLError as e:
    print(f'URLError: {e.reason}')
