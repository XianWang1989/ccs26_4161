
import requests

# Define the URL and authentication
url = "http://blabla.com:8080/job/myproject/config.xml"
auth = ('user', 'pass')

# Read the contents of new_config.xml
with open('new_config.xml', 'rb') as file:
    payload = file.read()  # Read the binary content

# Set the headers
headers = {"Content-Type": "application/xml"}

# Make the POST request
response = requests.post(url, auth=auth, data=payload, headers=headers)

# Check the response
print(response.status_code)  # Should be 200 or 204 for success
print(response.text)         # Display response if needed
