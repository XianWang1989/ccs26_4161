
import urllib2

# Define the URL and credentials
url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Create a password manager
password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
password_mgr.add_password(None, url, username, passwd)

# Create an authentication handler
auth_handler = urllib2.HTTPBasicAuthHandler(password_mgr)

# Create an opener that uses the authentication handler
opener = urllib2.build_opener(auth_handler)

# Install the opener
urllib2.install_opener(opener)

# Make the request
try:
    response = urllib2.urlopen(url)
    print(response.read())
except urllib2.HTTPError as e:
    print('HTTPError: {}'.format(e.code))
except urllib2.URLError as e:
    print('URLError: {}'.format(e.reason))
