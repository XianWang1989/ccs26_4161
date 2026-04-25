
import requests

url = "http://blabla.com:8080/job/myproject/config.xml"
auth = ('user', 'pass')

# Read the XML file content
with open('new_config.xml', 'rb') as file:
    payload = file.read()

headers = {
    "Content-Type": "application/xml"
}

# Make the POST request
response = requests.post(url, auth=auth, data=payload, headers=headers)

# Check the response
if response.status_code == 200:
    print("Success! Configuration updated.")
else:
    print(f"Failed with status code: {response.status_code}")
    print(response.text)
