
import requests

# Define the URL and authentication
url = "http://user:pass@blabla.com:8080/job/myproject/config.xml"

# Read the new configuration from the XML file
with open('new_config.xml', 'rb') as file:
    payload = file.read()

# Define headers
headers = {"Content-Type": "application/xml"}

# Make the POST request
r = requests.post(url, auth=('user', 'pass'), data=payload, headers=headers)

# Check the response
if r.status_code == 200:
    print("Configuration updated successfully!")
else:
    print(f"Failed to update configuration: {r.status_code} - {r.text}")
