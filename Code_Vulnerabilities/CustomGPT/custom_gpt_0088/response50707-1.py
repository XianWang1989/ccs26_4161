
import urllib2
import base64

# Define the URL and credentials
url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Create a password manager and add credentials
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
    print(f"HTTPError: {e.code} - {e.reason}")
except urllib2.URLError as e:
    print(f"URLError: {e.reason}")
