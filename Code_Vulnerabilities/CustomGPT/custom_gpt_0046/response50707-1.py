
import urllib2
import base64

# Define the URL and credentials
url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Encode credentials
credentials = '%s:%s' % (username, passwd)
b64credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

# Create the request and add the Authorization header
req = urllib2.Request(url)
req.add_header('Authorization', 'Basic %s' % b64credentials)

try:
    # Make the request
    response = urllib2.urlopen(req)
    print(response.read())  # Read and print the response
except urllib2.HTTPError as e:
    print('HTTP error:', e.code)
except urllib2.URLError as e:
    print('URL error:', e.reason)
