
import urllib2
import base64

url = 'http://example.com'  # Replace with your URL
username = 'your_username'    # Replace with your username
passwd = 'your_password'       # Replace with your password

# Encode username and password
credentials = '%s:%s' % (username, passwd)
b64credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

# Create the request and add the authorization header
req = urllib2.Request(url)
req.add_header('Authorization', 'Basic %s' % b64credentials)

try:
    response = urllib2.urlopen(req)
    print(response.read())  # Print the response from the server
except urllib2.HTTPError as e:
    print('HTTPError: {}'.format(e.code))
except urllib2.URLError as e:
    print('URLError: {}'.format(e.reason))
