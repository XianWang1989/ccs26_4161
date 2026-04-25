
import requests

url = "http://user:pass@blabla.com:8080/job/myproject/config.xml"

# Read the contents of the new_config.xml file
with open('new_config.xml', 'rb') as config_file:
    payload = config_file.read()

headers = {"Content-Type": "application/xml"}

# Make the POST request
response = requests.post(url, data=payload, headers=headers)

# Check the response
print(response.status_code)
print(response.content)
