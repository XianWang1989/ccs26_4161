
import urllib2
import base64

class CustomHTTPPasswordMgr(urllib2.HTTPPasswordMgrWithDefaultRealm):
    def add_password(self, realm, uri, user, passwd):
        auth = 'Basic {}'.format(base64.encodestring('{}:{}'.format(user, passwd)).strip())
        self.realm = realm
        self.uri = uri
        self.auth = auth

    def find_user_password(self, realm, uri):
        if self.realm == realm and self.uri == uri:
            return self.realm, self.auth
        return None, None

url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Create a password manager
password_mgr = CustomHTTPPasswordMgr()
password_mgr.add_password(None, url, username, passwd)

# Create an opener with the password manager
opener = urllib2.build_opener(urllib2.HTTPBasicAuthHandler(password_mgr))

# Open the URL
try:
    response = opener.open(url)
    print(response.read())
except urllib2.HTTPError as e:
    print('HTTP Error: {}'.format(e.code))
except urllib2.URLError as e:
    print('URL Error: {}'.format(e.reason))
