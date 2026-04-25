
import requests

# Define the URL and authentication
url = "http://user:pass@blabla.com:8080/job/myproject/config.xml"

# Read the config file contents
with open("new_config.xml", "rb") as file:
    config_data = file.read()

# Set the headers
headers = {"Content-Type": "application/xml"}

# Make the POST request
response = requests.post(url, auth=('user', 'pass'), data=config_data, headers=headers)

# Check the response
if response.status_code == 200:
    print("Config updated successfully.")
else:
    print(f"Failed to update config. Status Code: {response.status_code}")
