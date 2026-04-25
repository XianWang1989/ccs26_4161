
import requests

url = "http://blabla.com:8080/job/myproject/config.xml"
auth = ('user', 'pass')

# Read the new_config.xml file
with open('new_config.xml', 'rb') as file:
    config_data = file.read()

headers = {"Content-Type": "application/xml"}

# Send the POST request with the file content
r = requests.post(url, auth=auth, data=config_data, headers=headers)

# Print the response
print(r.status_code)
print(r.text)
