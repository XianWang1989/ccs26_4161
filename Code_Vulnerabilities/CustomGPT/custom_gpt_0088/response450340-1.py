
import requests

url = "http://blabla.com:8080/job/myproject/config.xml"
auth = ('user', 'pass')

# Read the content of the new_config.xml file
with open('new_config.xml', 'rb') as file:
    payload = file.read()

headers = {"Content-Type": "application/xml"}

# Send the POST request with the file content
response = requests.post(url, auth=auth, data=payload, headers=headers)

# Check the response
print(response.status_code)
print(response.text)
