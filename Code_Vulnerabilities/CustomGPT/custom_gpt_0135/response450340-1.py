
import requests

url = "http://blabla.com:8080/job/myproject/config.xml"
auth = ('user', 'pass')

# Open the new_config.xml file in binary mode
with open('new_config.xml', 'rb') as file:
    headers = {"Content-Type": "application/xml"}

    # Send the request
    response = requests.post(url, auth=auth, data=file, headers=headers)

# Check the response
print(f"Response Code: {response.status_code}")
print(f"Response Content: {response.content.decode()}")
