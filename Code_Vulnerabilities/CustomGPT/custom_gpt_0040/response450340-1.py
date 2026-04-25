
import requests

# Define the URL and authentication
url = "http://blabla.com:8080/job/myproject/config.xml"
auth = ('user', 'pass')

# Read the content of the new_config.xml file
with open('new_config.xml', 'rb') as file:
    config_data = file.read()

# Set headers
headers = {"Content-Type": "application/xml"}

# Make the POST request
response = requests.post(url, auth=auth, data=config_data, headers=headers)

# Print the response
print(f"Status Code: {response.status_code}")
print(f"Response: {response.text}")
