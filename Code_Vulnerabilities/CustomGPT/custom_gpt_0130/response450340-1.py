
import requests

url = "http://user:pass@blabla.com:8080/job/myproject/config.xml"

# Read the contents of the new_config.xml file
with open('new_config.xml', 'rb') as file:
    payload = file.read()

# Set the headers
headers = {"Content-Type": "application/xml"}

# Make the POST request
response = requests.post(url, data=payload, headers=headers)

# Check the response
print(f'Status Code: {response.status_code}')
print('Response:', response.content)
