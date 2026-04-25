
import requests

# Define the URL, authentication, and headers
url = "http://user:pass@blabla.com:8080/job/myproject/config.xml"
headers = {"Content-Type": "application/xml"}

# Read the contents of the new_config.xml file
with open('new_config.xml', 'rb') as f:
    payload = f.read()

# Send the POST request
response = requests.post(url, data=payload, headers=headers)

# Check the response
print("Status Code:", response.status_code)
print("Response:", response.text)
