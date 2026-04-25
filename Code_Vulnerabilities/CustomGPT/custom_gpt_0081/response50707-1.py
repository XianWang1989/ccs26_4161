
import urllib2
import base64

url = 'http://xxxx'  # Replace with the actual URL
username = 'jpx'
passwd = 'jpx123'
b64str = base64.b64encode(f'{username}:{passwd}'.encode()).decode()

req = urllib2.Request(url)
auth = f'Basic {b64str}'
req.add_header('Authorization', auth)

try:
    response = urllib2.urlopen(req)
    print(response.read())
except urllib2.HTTPError as e:
    print(f'HTTP error: {e.code}')
except urllib2.URLError as e:
    print(f'URL error: {e.reason}')
