
import urllib2
import base64

# Define the URL and credentials
url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Create a request object
request = urllib2.Request(url)

# Encode the credentials using base64
credentials = '%s:%s' % (username, passwd)
b64_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

# Add the Authorization header with the encoded credentials
request.add_header('Authorization', 'Basic %s' % b64_credentials)

try:
    # Make the request
    response = urllib2.urlopen(request)
    # Read and print the response
    print(response.read())
except urllib2.HTTPError as e:
    print("HTTP Error:", e.code, e.reason)
except urllib2.URLError as e:
    print("URL Error:", e.reason)
