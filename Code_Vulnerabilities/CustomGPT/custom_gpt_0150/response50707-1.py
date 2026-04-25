
import urllib2
import base64

url = 'http://xxxx'  # Replace with the actual URL
username = 'jpx'
passwd = 'jpx123'

# Encode the username and password
credentials = f'{username}:{passwd}'
b64_credentials = base64.b64encode(credentials.encode()).decode()

# Create the request and add the Authorization header
req = urllib2.Request(url)
req.add_header('Authorization', 'Basic ' + b64_credentials)

try:
    # Open the URL
    response = urllib2.urlopen(req)
    # Read response
    response_content = response.read()
    print(response_content)
except urllib2.HTTPError as e:
    print(f'HTTPError: {e.code} - {e.reason}')
except urllib2.URLError as e:
    print(f'URLError: {e.reason}')
