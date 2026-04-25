
import requests

url = "http://blabla.com:8080/job/myproject/config.xml"
auth = ('user', 'pass')

# Read the content of the new_config.xml file
with open('new_config.xml', 'r') as file:
    payload = file.read()

# Set the correct headers
headers = {"Content-Type": "application/xml"}

# Make the POST request
response = requests.post(url, auth=auth, data=payload, headers=headers)

# Print the response status code and any response text
print("Response Code:", response.status_code)
print("Response Body:", response.text)
