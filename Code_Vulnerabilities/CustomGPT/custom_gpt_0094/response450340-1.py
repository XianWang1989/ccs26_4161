
import requests

# Define the URL for the Jenkins job configuration
url = "http://blabla.com:8080/job/myproject/config.xml"

# Set the authentication credentials
auth = ('user', 'pass')

# Read the contents of the new_config.xml file
with open('new_config.xml', 'rb') as file:
    payload = file.read()

# Set the headers for the request
headers = {"Content-Type": "application/xml"}

# Make the POST request to update the config.xml
response = requests.post(url, auth=auth, data=payload, headers=headers)

# Print the response status code and content for debugging
print(response.status_code)
print(response.text)
