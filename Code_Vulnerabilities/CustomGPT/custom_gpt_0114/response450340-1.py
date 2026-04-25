
import requests

url = "http://blabla.com:8080/job/myproject/config.xml"
auth = ('user', 'pass')

# Read the content of the new_config.xml file
with open('new_config.xml', 'r') as file:
    payload = file.read()

# Set the headers for the request
headers = {
    "Content-Type": "application/xml"
}

# Make the POST request
r = requests.post(url, auth=auth, data=payload, headers=headers)

# Check the response
print(f'Status Code: {r.status_code}')
print(r.text)  # Optionally print the response for debugging
