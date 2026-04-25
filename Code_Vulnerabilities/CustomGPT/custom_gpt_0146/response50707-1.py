
import urllib2
import base64

# Details for authentication
url = 'http://xxxx'  # Replace with your URL
username = 'jpx'
passwd = 'jpx123'

# Encode username and password to Base64
credentials = '%s:%s' % (username, passwd)
b64_credentials = base64.encodestring(credentials.encode('utf-8')).decode('utf-8').strip()

# Create the request object
req = urllib2.Request(url)
auth = 'Basic %s' % b64_credentials
req.add_header('Authorization', auth)

# Open the URL with the request object
try:
    response = urllib2.urlopen(req)
    print(response.read())  # Print the response content
except urllib2.HTTPError as e:
    print("HTTP Error:", e.code)
    print(e.read())
except urllib2.URLError as e:
    print("URL Error:", e.reason)

