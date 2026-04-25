
import requests

url = "http://blabla.com:8080/job/myproject/config.xml"
auth = ('user', 'pass')

# Read the contents of new_config.xml
with open('new_config.xml', 'rb') as file:
    payload = file.read()

# Set the headers correctly
headers = {"Content-Type": "application/xml"}

# Send the POST request
r = requests.post(url, auth=auth, data=payload, headers=headers)

# Print the response for debugging
print(r.status_code)
print(r.text)
