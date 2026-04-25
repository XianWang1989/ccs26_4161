
import requests

# URL for the Jenkins job config
url = "http://blabla.com:8080/job/myproject/config.xml"

# Authentication credentials
auth = ('user', 'pass')

# Read the XML file
with open('new_config.xml', 'rb') as file:
    # Send the POST request with the contents of the file
    response = requests.post(url, auth=auth, data=file, headers={"Content-Type": "application/xml"})

# Check the response
if response.status_code == 200:
    print("Config updated successfully!")
else:
    print(f"Failed to update config: {response.status_code} - {response.text}")
