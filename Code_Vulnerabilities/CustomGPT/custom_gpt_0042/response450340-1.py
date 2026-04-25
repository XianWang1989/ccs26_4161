
import requests

# Define the URL and authentication
url = "http://user:pass@blabla.com:8080/job/myproject/config.xml"

# Read the new config from the XML file
with open("new_config.xml", "rb") as config_file:
    payload = config_file.read()  # Read the content of the XML file

# Define headers
headers = {"Content-Type": "application/xml"}

# Send the POST request
response = requests.post(url, data=payload, headers=headers)

# Check the response
if response.status_code == 200:
    print("Configuration updated successfully!")
else:
    print(f"Failed to update configuration. Status code: {response.status_code}")
    print(response.text)  # Print the response text for debugging
