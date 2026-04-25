
import urllib2
import base64

# Function to create a request with Authorization header
def get_authenticated_url(url, username, passwd):
    # Encode the username and password
    b64str = base64.b64encode(f'{username}:{passwd}'.encode()).decode()

    # Create a request object
    req = urllib2.Request(url)

    # Set the Authorization header
    auth = 'Basic %s' % b64str
    req.add_header('Authorization', auth)

    try:
        # Open the URL
        opener = urllib2.urlopen(req)
        return opener.read()  # Read and return the response
    except urllib2.HTTPError as e:
        print("HTTP Error:", e.code, e.read())
    except urllib2.URLError as e:
        print("URL Error:", e.reason)

# Example usage
url = 'http://xxxx'  # Replace with your URL
username = 'jpx'
passwd = 'jpx123'

response = get_authenticated_url(url, username, passwd)
print(response)
