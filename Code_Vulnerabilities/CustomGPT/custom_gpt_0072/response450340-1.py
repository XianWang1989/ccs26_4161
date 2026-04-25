
import requests

# Define the URL and authentication
url = "http://user:pass@blabla.com:8080/job/myproject/config.xml"

# Read the contents of the new_config.xml file
with open("new_config.xml", "rb") as f:
    payload = f.read()

# Set the headers
headers = {"Content-Type": "application/xml"}

# Make the POST request
response = requests.post(url, data=payload, headers=headers)

# Check the status code
print("Response Code:", response.status_code)
print("Response Body:", response.text)
