
import urllib2

# URL and credentials
url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Create a password manager
password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

# Add the username and password for the specified URL
password_mgr.add_password(None, url, username, passwd)

# Create an opener that uses the password manager
handler = urllib2.HTTPBasicAuthHandler(password_mgr)
opener = urllib2.build_opener(handler)

# Install the opener
urllib2.install_opener(opener)

# Now make a request to the URL
try:
    response = urllib2.urlopen(url)
    print(response.read())
except urllib2.HTTPError as e:
    print('HTTPError: {}'.format(e.code))
except urllib2.URLError as e:
    print('URLError: {}'.format(e.reason))
