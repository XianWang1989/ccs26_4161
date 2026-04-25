
import requests

url = "http://host:8080/job/myproject/config.xml"
auth = ('user', 'pass')

# Open the file in binary mode and send it as data
with open('new_config.xml', 'rb') as file:
    r = requests.post(url, auth=auth, data=file, headers={"Content-Type": "application/xml"})

# Check the response
print(r.status_code)
print(r.text)
