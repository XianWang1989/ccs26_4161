
import urllib2
import base64

# Define the URL and credentials
url = 'http://example.com'
username = 'jpx'
passwd = 'jpx123'

# Create a password manager
password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

# Add the username and password to the manager
password_mgr.add_password(None, url, username, passwd)

# Create an opener using the password manager
handler = urllib2.HTTPBasicAuthHandler(password_mgr)
opener = urllib2.build_opener(handler)

# Install the opener
urllib2.install_opener(opener)

# Make the request
try:
    response = opener.open(url)
    print(response.read())
except urllib2.URLError as e:
    print(f'Error: {e}')
