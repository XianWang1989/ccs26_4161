
import requests

url = "http://blabla.com:8080/job/myproject/config.xml"
auth = ('user', 'pass')

# Open and read the new configuration file
with open('new_config.xml', 'rb') as file:
    payload = file.read()

# Correct Content-Type header
headers = {"Content-Type": "application/xml"}

# Make the POST request
r = requests.post(url, auth=auth, data=payload, headers=headers)

# Check the response
if r.status_code == 200:
    print("Config updated successfully!")
else:
    print(f"Failed to update config: {r.status_code} - {r.text}")
