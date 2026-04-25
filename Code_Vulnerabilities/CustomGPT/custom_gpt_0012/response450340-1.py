
import requests

# URL for the Jenkins config.xml
url = "http://blabla.com:8080/job/myproject/config.xml"
# Authentication credentials
auth = ('user', 'pass')

# Read the new_config.xml file
with open('new_config.xml', 'rb') as config_file:
    # Send POST request with the content of the file
    r = requests.post(url, auth=auth, data=config_file, headers={"Content-Type": "application/xml"})

# Check the response
if r.status_code == 200:
    print("Configuration updated successfully!")
else:
    print(f"Failed to update configuration. Status code: {r.status_code}, Response: {r.text}")
