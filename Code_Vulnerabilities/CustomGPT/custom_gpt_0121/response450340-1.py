
import requests

# Define the URL and authentication
url = "http://blabla.com:8080/job/myproject/config.xml"
auth = ('user', 'pass')

# Read the new config from the file
with open('new_config.xml', 'rb') as f:
    payload = f.read()

# Set the headers
headers = {"Content-Type": "application/xml"}

# Send the POST request
response = requests.post(url, auth=auth, data=payload, headers=headers)

# Check the response
print(response.status_code)
print(response.text)
