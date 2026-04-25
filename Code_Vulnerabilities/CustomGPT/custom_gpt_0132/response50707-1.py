
import urllib2
import base64

def fetch_authenticated_url(url, username, password):
    # Create a request object
    req = urllib2.Request(url)

    # Encode username and password in base64
    auth = 'Basic %s' % base64.b64encode('%s:%s' % (username, password))

    # Add the Authorization header
    req.add_header('Authorization', auth)

    try:
        # Open the URL with the request
        response = urllib2.urlopen(req)
        return response.read()
    except urllib2.HTTPError as e:
        print('HTTPError: {}'.format(e.code))
    except urllib2.URLError as e:
        print('URLError: {}'.format(e.reason))

# Usage
url = 'http://xxxx'
username = 'jpx'
password = 'jpx123'
content = fetch_authenticated_url(url, username, password)

print(content)
