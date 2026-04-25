
import requests

# Define the URL and authentication
url = "http://user:pass@blabla.com:8080/job/myproject/config.xml"

# Read the contents of the new_config.xml file
with open("new_config.xml", "rb") as file:
    payload = file.read()

# Define the headers
headers = {"Content-Type": "application/xml"}

# Send the POST request
response = requests.post(url, data=payload, headers=headers)

# Check the response
if response.status_code == 200:
    print("Config updated successfully!")
else:
    print(f"Failed to update config. Status code: {response.status_code}")
    print(response.text)
