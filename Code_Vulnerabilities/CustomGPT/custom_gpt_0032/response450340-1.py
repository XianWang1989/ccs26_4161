
import requests

# URL and authentication details
url = "http://host:8080/job/myproject/config.xml"
auth = ('user', 'pass')

# Read the new configuration from the file
with open('new_config.xml', 'rb') as file:
    payload = file.read()

# Set the content type in headers
headers = {"Content-Type": "application/xml"}

# Make the POST request
r = requests.post(url, auth=auth, data=payload, headers=headers)

# Check the response
if r.status_code == 200:
    print("Configuration updated successfully!")
else:
    print(f"Failed to update configuration. Status code: {r.status_code}")
    print(r.text)  # Optional: Print the response for debugging
