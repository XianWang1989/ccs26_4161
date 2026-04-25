
import requests

# Define the URL and authentication credentials
url = "http://user:pass@blabla.com:8080/job/myproject/config.xml"

# Read the XML file content
with open('new_config.xml', 'r') as file:
    xml_data = file.read()

# Set the headers
headers = {"Content-Type": "application/xml"}

# Make the POST request
response = requests.post(url, data=xml_data, headers=headers)

# Check the response
print(f'Status Code: {response.status_code}')
print(f'Response: {response.text}')
