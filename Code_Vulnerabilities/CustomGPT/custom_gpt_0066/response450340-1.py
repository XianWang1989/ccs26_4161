
import requests

# Define your URL and authentication
url = "http://blabla.com:8080/job/myproject/config.xml"
auth = ('user', 'pass')

# Read the new config file
with open('new_config.xml', 'rb') as config_file:
    payload = config_file.read()  # Read the file contents

# Set headers
headers = {"Content-Type": "application/xml"}

# Make the POST request
response = requests.post(url, auth=auth, data=payload, headers=headers)

# Check the response
if response.status_code == 200:
    print("Configuration updated successfully!")
else:
    print("Failed to update configuration:", response.status_code, response.text)
