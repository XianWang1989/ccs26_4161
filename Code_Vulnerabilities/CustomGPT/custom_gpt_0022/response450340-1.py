
import requests

url = "http://blabla.com:8080/job/myproject/config.xml"
auth = ('user', 'pass')

# Read the XML file content
with open('new_config.xml', 'rb') as f:
    payload = f.read()

# Set headers
headers = {"Content-Type": "application/xml"}

# Send the POST request
r = requests.post(url, auth=auth, data=payload, headers=headers)

# Check response
print(r.status_code)
print(r.text)
