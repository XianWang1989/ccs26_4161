
import requests

# Define the URL, authentication, and headers
url = "http://blabla.com:8080/job/myproject/config.xml"
auth = ('user', 'pass')
headers = {"Content-Type": "application/xml"}

# Read the contents of the new_config.xml file
with open('new_config.xml', 'rb') as config_file:
    payload = config_file.read()

# Make the POST request
response = requests.post(url, auth=auth, data=payload, headers=headers)

# Check the response
print(f"Response Code: {response.status_code}")
print(f"Response Body: {response.text}")
