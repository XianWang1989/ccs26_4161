
import urllib2

url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Set up password manager
password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
password_mgr.add_password(None, url, username, passwd)

# Create an opener that uses the password manager
handler = urllib2.HTTPBasicAuthHandler(password_mgr)
opener = urllib2.build_opener(handler)

# Use the opener to fetch the URL
urllib2.install_opener(opener)

try:
    response = urllib2.urlopen(url)
    print(response.read())
except urllib2.HTTPError as e:
    print(f'HTTPError: {e.code} - {e.reason}')
except urllib2.URLError as e:
    print(f'URLError: {e.reason}')
