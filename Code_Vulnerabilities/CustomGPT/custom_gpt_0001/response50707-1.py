
import urllib2

# Configuration
url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Creating a password manager and adding the user's credentials
password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
password_mgr.add_password(None, url, username, passwd)

# Creating an authenticated opener
handler = urllib2.HTTPBasicAuthHandler(password_mgr)
opener = urllib2.build_opener(handler)

# Install the opener from the previous step
urllib2.install_opener(opener)

# Now request the URL, this will use the credentials provided
try:
    response = urllib2.urlopen(url)
    content = response.read()
    print(content)
except urllib2.HTTPError as e:
    print(f'HTTP error: {e.code} - {e.reason}')
except urllib2.URLError as e:
    print(f'URL error: {e.reason}')
