
import urllib2

# Setup password manager
password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
url = 'http://xxxx'  # Replace with the actual URL
username = 'jpx'
passwd = 'jpx123'

password_mgr.add_password(None, url, username, passwd)

# Create an auth handler using the password manager
auth_handler = urllib2.HTTPBasicAuthHandler(password_mgr)

# Build an opener with the auth handler
opener = urllib2.build_opener(auth_handler)

# Install the opener as the default opener
urllib2.install_opener(opener)

try:
    response = urllib2.urlopen(url)
    print(response.read())
except urllib2.HTTPError as e:
    print(f'HTTP error: {e.code}')
except urllib2.URLError as e:
    print(f'URL error: {e.reason}')
