
import urllib2
import base64

def fetch_url_with_auth(url, username, password):
    # Create a base64 encoded string of the credentials
    credentials = '%s:%s' % (username, password)
    b64_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

    # Create a request object and add the authentication header
    req = urllib2.Request(url)
    auth_header = 'Basic %s' % b64_credentials
    req.add_header('Authorization', auth_header)

    # Perform the request
    try:
        response = urllib2.urlopen(req)
        return response.read()
    except urllib2.HTTPError as e:
        print('HTTPError: {}'.format(e.code))
    except urllib2.URLError as e:
        print('URLError: {}'.format(e.reason))

# Usage example
url = 'http://xxxx'  # Replace with your URL
username = 'jpx'
password = 'jpx123'
content = fetch_url_with_auth(url, username, password)
print(content)
