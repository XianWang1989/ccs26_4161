
import requests

url = "http://user:pass@blabla.com:8080/job/myproject/config.xml"
headers = {"Content-Type": "application/xml"}

# Read the contents of the new_config.xml file
with open('new_config.xml', 'rb') as file:
    payload = file.read()

# Make the POST request
response = requests.post(url, data=payload, headers=headers)

# Print response status and content for debugging
print(response.status_code)
print(response.text)
