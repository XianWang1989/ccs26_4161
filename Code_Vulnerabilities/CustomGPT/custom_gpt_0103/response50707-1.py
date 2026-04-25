
import urllib2

# Define the URL and credentials
url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Set up password manager and authentication handler
password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
password_mgr.add_password(None, url, username, passwd)

auth_handler = urllib2.HTTPBasicAuthHandler(password_mgr)
opener = urllib2.build_opener(auth_handler)

# Install the opener
urllib2.install_opener(opener)

# Make the request
try:
    response = urllib2.urlopen(url)
    print(response.read())
except urllib2.HTTPError as e:
    print(f'HTTPError: {e.code} - {e.reason}')
except urllib2.URLError as e:
    print(f'URLError: {e.reason}')
