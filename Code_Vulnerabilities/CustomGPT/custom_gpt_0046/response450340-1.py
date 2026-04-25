
import requests

# URL and authentication details
url = "http://blabla.com:8080/job/myproject/config.xml"
auth = ('user', 'pass')

# Read the contents of the new_config.xml file
with open('new_config.xml', 'rb') as f:
    payload = f.read()

# Set the headers
headers = {"Content-Type": "application/xml"}

# Make the POST request
response = requests.post(url, auth=auth, data=payload, headers=headers)

# Check the response
print("Response Code:", response.status_code)
print("Response Body:", response.text)
