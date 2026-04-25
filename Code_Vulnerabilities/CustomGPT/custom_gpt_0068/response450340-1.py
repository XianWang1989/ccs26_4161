
import requests

# Define the URL and authentication
url = "http://user:pass@blabla.com:8080/job/myproject/config.xml"

# Read the contents of the XML file
with open("new_config.xml", "rb") as file:
    payload = file.read()

# Set headers
headers = {"Content-Type": "application/xml"}

# Make the POST request
response = requests.post(url, data=payload, headers=headers)

# Print response for debugging
print(f"Response Code: {response.status_code}")
print(f"Response Body: {response.text}")
