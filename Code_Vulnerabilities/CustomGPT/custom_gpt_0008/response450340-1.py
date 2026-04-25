
import requests

url = "http://user:pass@blabla.com:8080/job/myproject/config.xml"

# Read the content of the new config file
with open("new_config.xml", "rb") as file:
    payload = file.read()

# Set the headers for the request
headers = {"Content-Type": "application/xml"}

# Make the POST request
response = requests.post(url, data=payload, headers=headers)

# Check the response
if response.status_code == 200:
    print("Configuration updated successfully.")
else:
    print(f"Failed to update configuration. Status code: {response.status_code}")
    print("Response:", response.text)
