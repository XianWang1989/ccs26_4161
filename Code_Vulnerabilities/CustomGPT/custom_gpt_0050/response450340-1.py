
import requests

url = "http://blabla.com:8080/job/myproject/config.xml"
auth = ('user', 'pass')

# Read the content of the new_config.xml file
with open('new_config.xml', 'rb') as file:
    response = requests.post(url, auth=auth, data=file, headers={"Content-Type": "application/xml"})

# Check the response
print(response.status_code)
if response.status_code == 200:
    print("Config updated successfully!")
else:
    print("Failed to update config:", response.text)
