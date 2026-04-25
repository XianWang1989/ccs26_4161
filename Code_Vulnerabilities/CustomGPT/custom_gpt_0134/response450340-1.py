
import requests

url = "http://blabla.com:8080/job/myproject/config.xml"
auth = ('user', 'pass')

# Read the XML file
with open('new_config.xml', 'rb') as file:
    # Send the POST request
    response = requests.post(url, auth=auth, data=file, headers={"Content-Type": "application/xml"})

# Check the response
print("Response Code:", response.status_code)
print("Response Body:", response.text)
