
import requests

url = "http://blabla.com:8080/job/myproject/config.xml"
auth = ('user', 'pass')

# Load the new configuration from the XML file
with open('new_config.xml', 'rb') as file:
    payload = file.read()

# Set the appropriate headers
headers = {"Content-Type": "application/xml"}

# Make the POST request
r = requests.post(url, auth=auth, data=payload, headers=headers)

# Check the response
if r.status_code == 200:
    print("Configuration updated successfully.")
else:
    print(f"Failed to update configuration. Status code: {r.status_code}, Response: {r.text}")
