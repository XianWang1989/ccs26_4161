
import urllib2
import base64

def request_with_auth(url, username, password):
    # Encode the credentials
    credentials = f"{username}:{password}"
    b64_credentials = base64.b64encode(credentials.encode()).decode()

    # Create the request and add the authorization header
    req = urllib2.Request(url)
    req.add_header('Authorization', f'Basic {b64_credentials}')

    try:
        response = urllib2.urlopen(req)
        return response.read()  # Return the response data
    except urllib2.HTTPError as e:
        print(f"HTTP error occurred: {e.code} {e.reason}")
    except urllib2.URLError as e:
        print(f"URL error occurred: {e.reason}")

# Usage
url = 'http://xxxx'  # Replace with your URL
username = 'jpx'
password = 'jpx123'

response_data = request_with_auth(url, username, password)
print(response_data)
