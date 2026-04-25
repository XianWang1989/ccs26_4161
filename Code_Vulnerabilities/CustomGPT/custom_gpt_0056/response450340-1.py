
import requests

# URL for the Jenkins job config
url = "http://blabla.com:8080/job/myproject/config.xml"

# Authentication details
auth = ('user', 'pass')

# Read the content of the new_config.xml file
with open('new_config.xml', 'r') as file:
    payload = file.read()

# Set headers
headers = {"Content-Type": "application/xml"}

# Make the POST request to update the config
response = requests.post(url, auth=auth, data=payload, headers=headers)

# Check the response
if response.status_code == 200:
    print("Config updated successfully.")
else:
    print(f"Failed to update config. Status code: {response.status_code}, Response: {response.text}")
