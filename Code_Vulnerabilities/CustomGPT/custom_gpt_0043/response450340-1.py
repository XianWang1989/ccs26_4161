
import requests

url = "http://blabla.com:8080/job/myproject/config.xml"
auth = ('user', 'pass')

# Read the contents of new_config.xml
with open('new_config.xml', 'rb') as file:
    payload = file.read()  # Read the file's contents as bytes

headers = {"Content-Type": "application/xml"}

# Perform the POST request
r = requests.post(url, auth=auth, data=payload, headers=headers)

# Print the response
print(f"Response code: {r.status_code}")
print(f"Response body: {r.text}")
