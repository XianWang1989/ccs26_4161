
import requests

url = "http://blabla.com:8080/job/myproject/config.xml"
auth = ('user', 'pass')

# Read the contents of new_config.xml
with open('new_config.xml', 'rb') as file:
    payload = file.read()

# Set headers to indicate the content type
headers = {"Content-Type": "application/xml"}

# Make the POST request to update the config.xml
r = requests.post(url, auth=auth, data=payload, headers=headers)

# Check the response
if r.status_code == 200:
    print("Config updated successfully.")
else:
    print(f"Failed to update config. Status code: {r.status_code}, Response: {r.text}")
