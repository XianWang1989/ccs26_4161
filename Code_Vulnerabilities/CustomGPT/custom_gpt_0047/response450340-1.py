
import requests

url = "http://blabla.com:8080/job/myproject/config.xml"
auth = ('user', 'pass')

# Open the new_config.xml file in binary mode
with open('new_config.xml', 'rb') as file:
    # Send the POST request with the file content
    r = requests.post(url, auth=auth, data=file, headers={"Content-Type": "application/xml"})

# Check the response
if r.status_code == 200:
    print("Configuration updated successfully.")
else:
    print(f"Failed to update configuration: {r.status_code}, {r.text}")
