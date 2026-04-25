
import requests

# Define URL and authentication
url = "http://blabla.com:8080/job/myproject/config.xml"
auth = ('user', 'pass')

# Read the new config file
with open('new_config.xml', 'rb') as file:
    payload = file.read()

# Set headers
headers = {"Content-Type": "application/xml"}

# Make the POST request
response = requests.post(url, auth=auth, data=payload, headers=headers)

# Print the response
print(response.status_code)
print(response.text)  # Optionally print the response body for more details
