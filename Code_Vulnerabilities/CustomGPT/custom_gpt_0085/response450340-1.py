
import requests

# Define the URL and authentication credentials
url = "http://blabla.com:8080/job/myproject/config.xml"
auth = ('user', 'pass')

# Read the contents of the new config file
with open('new_config.xml', 'rb') as file:
    payload = file.read()

# Set the headers
headers = {"Content-Type": "application/xml"}

# Make the POST request to Jenkins
response = requests.post(url, auth=auth, data=payload, headers=headers)

# Print the response status
print("Response Code:", response.status_code)
if response.status_code != 200:
    print("Error:", response.text)
