
import requests

url = "http://blabla.com:8080/job/myproject/config.xml"
auth = ('user', 'pass')

# Read the contents of the config file
with open('new_config.xml', 'rb') as config_file:
    payload = config_file.read()  # Read the file content in binary mode

# Set the appropriate headers
headers = {"Content-Type": "application/xml"}

# Make the POST request
response = requests.post(url, auth=auth, data=payload, headers=headers)

# Check the response
if response.status_code == 200:
    print("Config updated successfully!")
else:
    print(f"Failed to update config: {response.status_code}, {response.text}")
