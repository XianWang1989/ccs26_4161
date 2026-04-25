
import requests

url = "http://blabla.com:8080/job/myproject/config.xml"
auth = ('user', 'pass')

# Read the contents of the new_config.xml file
with open('new_config.xml', 'rb') as file:
    payload = file.read()

# Set the headers for the request
headers = {"Content-Type": "application/xml"}

# Make the POST request
response = requests.post(url, auth=auth, data=payload, headers=headers)

# Check the response
print(response.status_code)
print(response.text)
