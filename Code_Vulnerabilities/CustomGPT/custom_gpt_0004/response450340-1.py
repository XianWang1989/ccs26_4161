
import requests

url = "http://blabla.com:8080/job/myproject/config.xml"
auth = ('user', 'pass')

# Read the contents of the XML file
with open('new_config.xml', 'r') as file:
    config_data = file.read()

# Set the headers
headers = {"Content-Type": "application/xml"}

# Send the POST request
response = requests.post(url, auth=auth, data=config_data, headers=headers)

# Check the response
if response.status_code == 200:
    print("Config updated successfully.")
else:
    print(f"Failed to update config. Status code: {response.status_code}")
