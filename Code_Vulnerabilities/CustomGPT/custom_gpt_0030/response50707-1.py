
import urllib2
import base64

def make_authenticated_request(url, username, passwd):
    # Encode the username and password
    b64str = base64.b64encode(f'{username}:{passwd}'.encode()).decode()

    # Create the request object
    req = urllib2.Request(url)

    # Add the Authorization header
    req.add_header('Authorization', 'Basic %s' % b64str)

    try:
        # Make the request
        response = urllib2.urlopen(req)
        return response.read()
    except urllib2.HTTPError as e:
        print(f'HTTPError: {e.code} - {e.reason}')
    except urllib2.URLError as e:
        print(f'URLError: {e.reason}')

# Example usage
url = 'http://example.com/resource'
username = 'jpx'
passwd = 'jpx123'
response_content = make_authenticated_request(url, username, passwd)
print(response_content)
