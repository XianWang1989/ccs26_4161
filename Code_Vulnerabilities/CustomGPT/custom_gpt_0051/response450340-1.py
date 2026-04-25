
import requests

url = "http://blabla.com:8080/job/myproject/config.xml"
auth = ('user', 'pass')

# Read the contents of new_config.xml
with open('new_config.xml', 'rb') as file:  # Open in binary mode
    payload = file.read()

# Set the headers
headers = {"Content-Type": "application/xml"}

# Make the POST request
r = requests.post(url, auth=auth, data=payload, headers=headers)

# Check the response
print(f"Response Code: {r.status_code}")
print(r.text)  # Optionally print the response content
