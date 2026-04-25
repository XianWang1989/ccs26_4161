
import requests

# Define the URL and authentication details
url = "http://blabla.com:8080/job/myproject/config.xml"
auth = ('user', 'pass')

# Read the contents of the config file
with open("new_config.xml", 'rb') as config_file:
    payload = config_file.read()

# Set the appropriate headers
headers = {"Content-Type": "application/xml"}

# Make the POST request
response = requests.post(url, auth=auth, data=payload, headers=headers)

# Check the response
print("Response Code:", response.status_code)
print("Response Body:", response.text)
