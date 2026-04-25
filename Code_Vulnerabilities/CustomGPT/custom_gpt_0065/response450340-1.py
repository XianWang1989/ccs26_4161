
import requests

url = "http://user:pass@blabla.com:8080/job/myproject/config.xml"

# Read the contents of the new_config.xml
with open('new_config.xml', 'rb') as file:
    payload = file.read()

headers = {"Content-Type": "application/xml"}

# Make the POST request
r = requests.post(url, data=payload, headers=headers)

if r.status_code == 200:
    print("Successfully updated config.xml")
else:
    print(f"Failed to update config.xml: {r.status_code} - {r.text}")
