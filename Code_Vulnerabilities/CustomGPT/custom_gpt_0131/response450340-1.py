
import requests

url = "http://blabla.com:8080/job/myproject/config.xml"
auth = ('user', 'pass')

# Open the new_config.xml file and read its content
with open('new_config.xml', 'rb') as file:
    payload = file.read()

headers = {"Content-Type": "application/xml"}

# Send the post request
r = requests.post(url, auth=auth, data=payload, headers=headers)

# Check the response
print(r.status_code)
print(r.text)
