
import urllib2
import base64

# URL and credentials
url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Encode credentials
credentials = base64.b64encode(f'{username}:{passwd}'.encode()).decode()

# Create request
req = urllib2.Request(url)
req.add_header('Authorization', 'Basic ' + credentials)

# Make the request
try:
    response = urllib2.urlopen(req)
    print(response.read())
except urllib2.HTTPError as e:
    print('HTTPError: {}'.format(e.code))
except urllib2.URLError as e:
    print('URLError: {}'.format(e.reason))
