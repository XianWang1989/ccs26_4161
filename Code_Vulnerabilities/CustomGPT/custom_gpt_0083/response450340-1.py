
import requests

url = "http://user:pass@blabla.com:8080/job/myproject/config.xml"

# Read the content of the new_config.xml file
with open('new_config.xml', 'rb') as file:
    payload = file.read()

headers = {"Content-Type": "application/xml"}

# Send the POST request
r = requests.post(url, data=payload, headers=headers)

# Check the response
print(r.status_code)
print(r.text)
