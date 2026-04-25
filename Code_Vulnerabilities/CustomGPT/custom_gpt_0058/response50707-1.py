
import urllib2
import base64

# Define the URL and credentials
url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Encode the credentials in Base64
credentials = f'{username}:{passwd}'
b64_credentials = base64.encodestring(credentials.encode('utf-8')).decode('utf-8').strip()

# Create the request and add the Authorization header
req = urllib2.Request(url)
req.add_header('Authorization', 'Basic %s' % b64_credentials)

# Open the URL with the prepared request
try:
    opener = urllib2.urlopen(req)
    # Read the response
    response = opener.read()
    print(response)
except urllib2.HTTPError as e:
    print(f'HTTPError: {e.code} - {e.reason}')
except urllib2.URLError as e:
    print(f'URLError: {e.reason}')
