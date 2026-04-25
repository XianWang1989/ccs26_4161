
import requests

# URL and authentication
url = "http://user:pass@blabla.com:8080/job/myproject/config.xml"

# Read the new configuration from the XML file
with open('new_config.xml', 'rb') as file:
    payload = file.read()

# Set the headers
headers = {"Content-Type": "application/xml"}

# Make the POST request
response = requests.post(url, data=payload, headers=headers)

# Check the response
if response.status_code == 200:
    print("Configuration updated successfully.")
else:
    print(f"Failed to update configuration: {response.status_code} - {response.text}")
