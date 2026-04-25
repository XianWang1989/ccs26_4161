
import requests

# Define the URL and authentication
url = "http://user:pass@blabla.com:8080/job/myproject/config.xml"
auth = ('user', 'pass')

# Read the new config file content
with open('new_config.xml', 'rb') as file:
    data = file.read()

# Set headers
headers = {"Content-Type": "application/xml"}

# Make the POST request
response = requests.post(url, auth=auth, data=data, headers=headers)

# Check the response
print(response.status_code)
print(response.text)
