
import requests

# Set the URL and authentication
url = "http://blabla.com:8080/job/myproject/config.xml"
auth = ('user', 'pass')

# Open and read the new_config.xml file
with open("new_config.xml", 'rb') as file:
    # Send the POST request
    response = requests.post(url, auth=auth, data=file, headers={"Content-Type": "application/xml"})

# Check the response
if response.status_code == 200:
    print("Config updated successfully.")
else:
    print(f"Failed to update config. Status code: {response.status_code}. Response: {response.text}")
