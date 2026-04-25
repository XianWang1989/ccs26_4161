
import urllib2
import base64

# Define the authentication details
url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Encode the username and password
credentials = '%s:%s' % (username, passwd)
b64_credentials = base64.b64encode(credentials.encode()).decode()

# Create the request with the Authorization header
req = urllib2.Request(url)
req.add_header('Authorization', 'Basic %s' % b64_credentials)

try:
    # Make the request
    response = urllib2.urlopen(req)
    print(response.read())  # Process the response
except urllib2.HTTPError as e:
    print("HTTP Error: ", e.code)
except urllib2.URLError as e:
    print("URL Error: ", e.reason)
