
import requests

# Define the URL, authentication, and headers
url = "http://blabla.com:8080/job/myproject/config.xml"
auth = ('user', 'pass')
headers = {"Content-Type": "application/xml"}

# Read the contents of the new_config.xml
with open('new_config.xml', 'rb') as file:
    payload = file.read()  # Read the entire file as binary

# Make the POST request
response = requests.post(url, auth=auth, data=payload, headers=headers)

# Check the response
if response.status_code == 200:
    print("Configuration updated successfully.")
else:
    print(f"Failed to update configuration. Status code: {response.status_code}")
    print(f"Response: {response.text}")
