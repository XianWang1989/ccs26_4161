
import urllib2
import base64

url = 'http://example.com'  # Replace with your URL
username = 'your_username'   # Replace with your username
passwd = 'your_password'      # Replace with your password

# Encode the username and password
credentials = '%s:%s' % (username, passwd)
b64_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

# Create the request and add the Authorization header
request = urllib2.Request(url)
request.add_header('Authorization', 'Basic %s' % b64_credentials)

try:
    # Open the URL with the request
    response = urllib2.urlopen(request)
    # Read the response
    content = response.read()
    print(content)
except urllib2.HTTPError as e:
    # Handle HTTP errors
    print("HTTP Error: ", e.code)
except urllib2.URLError as e:
    # Handle URL errors
    print("URL Error: ", e.reason)
