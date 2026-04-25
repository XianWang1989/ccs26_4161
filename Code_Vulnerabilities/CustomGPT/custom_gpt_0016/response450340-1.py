
import requests

# Define URL and authentication
url = "http://blabla.com:8080/job/myproject/config.xml"
auth = ('user', 'pass')

# Read the XML file to be uploaded
with open('new_config.xml', 'r') as file:
    payload = file.read()  # Read the entire content of the XML file

# Set headers
headers = {'Content-Type': 'application/xml'}

# Make the POST request
response = requests.post(url, auth=auth, data=payload, headers=headers)

# Check the response status code
print(f"Response Code: {response.status_code}")
print(f"Response Body: {response.text}")
