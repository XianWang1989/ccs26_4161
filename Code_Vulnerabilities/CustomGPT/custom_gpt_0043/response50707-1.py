
import urllib2

# Define the URL, username, and password
url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Create a password manager
password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

# Add your username and password for the specified URL
password_mgr.add_password(None, url, username, passwd)

# Create an authentication handler
auth_handler = urllib2.HTTPBasicAuthHandler(password_mgr)

# Create an opener with the authentication handler
opener = urllib2.build_opener(auth_handler)

# Use the opener to make the request
urllib2.install_opener(opener)

# Make the request and read the response
try:
    response = urllib2.urlopen(url)
    content = response.read()
    print(content)
except urllib2.HTTPError as e:
    print("HTTPError: ", e.code)
except urllib2.URLError as e:
    print("URLError: ", e.reason)
