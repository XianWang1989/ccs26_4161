
import requests

url = "http://blabla.com:8080/job/myproject/config.xml"
auth = ('user', 'pass')

# Read the contents of the new_config.xml file
with open('new_config.xml', 'rb') as file:
    payload = file.read()

# Set the headers
headers = {"Content-Type": "application/xml"}

# Make the request
response = requests.post(url, auth=auth, data=payload, headers=headers)

# Check the response
print(f'Status Code: {response.status_code}')
print(f'Response Body: {response.text}')
