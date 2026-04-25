
import requests

# Define your URL and authentication
url = "http://user:pass@blabla.com:8080/job/myproject/config.xml"

# Read the contents of the new_config.xml file
with open('new_config.xml', 'rb') as file:
    payload = file.read()

# Define the headers
headers = {"Content-Type": "application/xml"}

# Make the POST request
response = requests.post(url, data=payload, headers=headers)

# Print the response for debugging
print(response.status_code)
print(response.text)
