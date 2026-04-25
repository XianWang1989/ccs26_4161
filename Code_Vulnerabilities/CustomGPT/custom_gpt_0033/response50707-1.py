
import urllib2
from urllib2 import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener, install_opener

# Set up credentials
url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Create a password manager
password_mgr = HTTPPasswordMgrWithDefaultRealm()
password_mgr.add_password(None, url, username, passwd)

# Create an authentication handler
auth_handler = HTTPBasicAuthHandler(password_mgr)

# Build an opener with the authentication handler
opener = build_opener(auth_handler)

# Install the opener
install_opener(opener)

# Now perform the request
try:
    response = opener.open(url)
    print(response.read())
except urllib2.HTTPError as e:
    print(f'HTTPError: {e.code} - {e.reason}')
except urllib2.URLError as e:
    print(f'URLError: {e.reason}')
