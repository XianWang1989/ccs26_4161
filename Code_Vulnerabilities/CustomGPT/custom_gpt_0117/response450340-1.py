
import requests

# Specify your Jenkins server URL
url = "http://blabla.com:8080/job/myproject/config.xml"

# Authentication credentials
auth = ('user', 'pass')

# Read the contents of new_config.xml and send as data
with open('new_config.xml', 'rb') as f:
    # Send a POST request
    headers = {"Content-Type": "application/xml"}
    response = requests.post(url, auth=auth, data=f, headers=headers)

# Check the response
if response.status_code == 200:
    print("Configuration updated successfully.")
else:
    print(f"Failed to update configuration. Status code: {response.status_code}")
    print("Response:", response.text)
