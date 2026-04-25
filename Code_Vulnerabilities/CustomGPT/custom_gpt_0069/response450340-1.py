
import requests

# Define the URL, username, and password for Jenkins authentication
url = "http://blabla.com:8080/job/myproject/config.xml"
auth = ('user', 'pass')

# Read the XML content from the file
with open("new_config.xml", 'rb') as file:
    payload = file.read()

# Set the headers to indicate the content type
headers = {"Content-Type": "application/xml"}

# Make the POST request to update the Jenkins config
response = requests.post(url, auth=auth, data=payload, headers=headers)

# Check the response status
if response.status_code == 200:
    print("Config updated successfully.")
else:
    print(f"Failed to update config. Status code: {response.status_code}, Response: {response.text}")
