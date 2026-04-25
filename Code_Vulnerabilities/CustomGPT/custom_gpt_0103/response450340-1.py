
import requests

# Define the URL and authentication
url = "http://blabla.com:8080/job/myproject/config.xml"
auth = ('user', 'pass')

# Read the new config file
with open('new_config.xml', 'rb') as file:
    payload = file.read()

# Set the headers
headers = {"Content-Type": "application/xml"}

# Make the POST request
response = requests.post(url, auth=auth, data=payload, headers=headers)

# Check the response
if response.status_code == 200:
    print("Config updated successfully!")
else:
    print(f"Failed to update config: {response.status_code}, {response.text}")
