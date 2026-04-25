
import urllib2
import base64

# Basic configuration
url = 'http://your-url-here'
username = 'your-username-here'
passwd = 'your-password-here'

# Create a password manager and add the username and password
password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
password_mgr.add_password(None, url, username, passwd)

# Create an authentication handler
auth_handler = urllib2.HTTPBasicAuthHandler(password_mgr)

# Create an opener that adds the authentication handler
opener = urllib2.build_opener(auth_handler)

# Install the opener as the default opener
urllib2.install_opener(opener)

# Make the request
req = urllib2.Request(url)

try:
    # Open the URL
    response = urllib2.urlopen(req)

    # Read and print the response
    print(response.read())
except urllib2.HTTPError as e:
    print('HTTPError: {}'.format(e.code))
except urllib2.URLError as e:
    print('URLError: {}'.format(e.reason))
