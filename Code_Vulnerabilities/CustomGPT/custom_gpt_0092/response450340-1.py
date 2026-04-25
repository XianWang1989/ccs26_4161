
import requests

# URL and authentication
url = "http://user:pass@blabla.com:8080/job/myproject/config.xml"

# Read the content of new_config.xml
with open('new_config.xml', 'rb') as file:  # Use 'rb' for binary mode
    payload = file.read()

# Set headers
headers = {"Content-Type": "application/xml"}

# Make the POST request
response = requests.post(url, data=payload, headers=headers)

# Check response
print(f'Status Code: {response.status_code}')
print(f'Response: {response.text}')
