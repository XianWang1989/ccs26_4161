
import urllib2
import base64

def request_with_auth(url, username, password):
    # Encode credentials
    credentials = '%s:%s' % (username, password)
    b64_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

    # Create the request object
    req = urllib2.Request(url)

    # Manually set the Authorization header
    auth_header = 'Basic %s' % b64_credentials
    req.add_header('Authorization', auth_header)

    try:
        # Open the URL with the Authorization header
        opener = urllib2.urlopen(req)
        # Read and return the response
        return opener.read()
    except IOError as e:
        # Handle errors (such as HTTPError)
        print(str(e))

# Example usage
url = 'http://xxxx'  # Replace with your URL
username = 'jpx'
password = 'jpx123'
response = request_with_auth(url, username, password)
print(response)
