
import requests

url = "http://blabla.com:8080/job/myproject/config.xml"
auth = ('user', 'pass')

# Read the contents of the new_config.xml file
with open('new_config.xml', 'rb') as file:
    payload = file.read()

headers = {"Content-Type": "application/xml"}

# Make the POST request with the binary data
response = requests.post(url, auth=auth, data=payload, headers=headers)

# Check response status
if response.status_code == 200:
    print("Config updated successfully.")
else:
    print(f"Failed to update config. Status code: {response.status_code}, Response: {response.text}")
