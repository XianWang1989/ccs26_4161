
import urllib2
import base64

url = 'http://xxxx'  # Replace with your URL
username = 'jpx'
passwd = 'jpx123'

# Create a base64 encoded string for the credentials
credentials = '%s:%s' % (username, passwd)
b64_credentials = base64.b64encode(credentials.encode()).decode()

# Create a request and add the Authorization header
req = urllib2.Request(url)
req.add_header('Authorization', 'Basic %s' % b64_credentials)

try:
    # Open the URL
    response = urllib2.urlopen(req)
    print(response.read())  # Read and print the response
except urllib2.HTTPError as e:
    print(f'HTTPError: {e.code} - {e.reason}')
except urllib2.URLError as e:
    print(f'URLError: {e.reason}')
