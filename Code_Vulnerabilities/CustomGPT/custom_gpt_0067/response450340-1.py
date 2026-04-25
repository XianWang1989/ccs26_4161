
import requests

url = "http://user:pass@blabla.com:8080/job/myproject/config.xml"

# Read the XML file
with open("new_config.xml", 'rb') as config_file:
    payload = config_file.read()

headers = {"Content-Type": "application/xml"}

# Send the POST request
r = requests.post(url, data=payload, headers=headers)

# Check response
if r.status_code == 200:
    print("Config updated successfully!")
else:
    print(f"Failed to update config: {r.status_code}, {r.text}")
