
import requests

# Define your URL and authentication
url = "http://blabla.com:8080/job/myproject/config.xml"
auth = ('user', 'pass')

# Open the new_config.xml file and read its contents
with open("new_config.xml", "rb") as config_file:
    # Use the read content as the data payload
    payload = config_file.read()

# Set the headers, note the Content-Type for XML
headers = {"Content-Type": "application/xml"}

# Make the POST request to update the configuration
response = requests.post(url, auth=auth, data=payload, headers=headers)

# Check the response status and print the result
if response.status_code == 200:
    print("Configuration updated successfully.")
else:
    print(f"Failed to update configuration. Status code: {response.status_code}, Response: {response.text}")
