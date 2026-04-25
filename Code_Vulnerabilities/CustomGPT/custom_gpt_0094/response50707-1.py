
import urllib2
import base64

# Function to create an authenticated request
def authenticated_request(url, username, passwd):
    b64str = base64.encodestring(f'{username}:{passwd}').strip()  # Encode credentials

    req = urllib2.Request(url)
    auth = 'Basic %s' % b64str
    req.add_header('Authorization', auth)  # Add the Authorization header

    try:
        response = urllib2.urlopen(req)  # Only one request
        return response.read()  # Return the response
    except urllib2.HTTPError as e:
        print(f'HTTPError: {e.code} - {e.reason}')
    except urllib2.URLError as e:
        print(f'URLError: {e.reason}')

# Usage
url = 'http://example.com'
username = 'jpx'
passwd = 'jpx123'
response_content = authenticated_request(url, username, passwd)
print(response_content)
