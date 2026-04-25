
import requests

# Define the URL and authentication
url = "http://blabla.com:8080/job/myproject/config.xml"
auth = ('user', 'pass')

# Read the contents of the new_config.xml file
with open('new_config.xml', 'rb') as file:
    payload = file.read()  # Read the file contents as bytes

# Set the headers
headers = {"Content-Type": "application/xml"}

# Send the POST request
response = requests.post(url, auth=auth, data=payload, headers=headers)

# Check the response
if response.status_code == 200:
    print("Configuration updated successfully.")
else:
    print(f"Failed to update configuration. Status Code: {response.status_code}. Response: {response.text}")
