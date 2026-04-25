
import requests

url = "http://blabla.com:8080/job/myproject/config.xml"
auth = ('user', 'pass')

# Read the contents of the config file
with open('new_config.xml', 'rb') as file:
    payload = file.read()

headers = {"Content-Type": "application/xml"}

# Send the POST request
r = requests.post(url, auth=auth, data=payload, headers=headers)

# Check the response
print(f"Response Code: {r.status_code}")
print(f"Response Body: {r.text}")
