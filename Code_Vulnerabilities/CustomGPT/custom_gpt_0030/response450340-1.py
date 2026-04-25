
import requests

# Define the URL and authentication
url = "http://blabla.com:8080/job/myproject/config.xml"
auth = ('user', 'pass')

# Read the XML file as binary data
with open("new_config.xml", "rb") as file:
    payload = file.read()

# Set headers
headers = {"Content-Type": "application/xml"}

# Make the POST request
r = requests.post(url, auth=auth, data=payload, headers=headers)

# Check the response
if r.status_code == 200:
    print("Configuration updated successfully.")
else:
    print(f"Failed to update configuration: {r.status_code} - {r.text}")
