
import requests

# Define the URL and authentication
url = "http://user:pass@blabla.com:8080/job/myproject/config.xml"

# Read the content of the new_config.xml file
with open('new_config.xml', 'rb') as file:
    payload = file.read()

# Set the headers
headers = {"Content-Type": "application/xml"}

# Make the POST request
response = requests.post(url, data=payload, headers=headers)

# Check the response status
if response.status_code == 200:
    print("Config updated successfully!")
else:
    print(f"Failed to update config. Status code: {response.status_code}")
    print(f"Response: {response.text}")
