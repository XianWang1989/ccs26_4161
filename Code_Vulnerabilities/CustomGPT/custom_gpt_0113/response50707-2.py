
import urllib2

# Setup for password manager
password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
password_mgr.add_password(None, 'http://example.com', 'jpx', 'jpx123')

# Create an opener that uses the password manager
opener = urllib2.build_opener(urllib2.HTTPBasicAuthHandler(password_mgr))

# Install the opener
urllib2.install_opener(opener)

# Make the request (this will still result in two requests)
try:
    response = urllib2.urlopen(url)
    print(response.read())
except urllib2.HTTPError as e:
    print('HTTPError: {}'.format(e.code))
except urllib2.URLError as e:
    print('URLError: {}'.format(e.reason))
