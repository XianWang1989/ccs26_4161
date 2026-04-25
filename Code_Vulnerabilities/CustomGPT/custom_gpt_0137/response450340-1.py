
import requests

# Define the URL and authentication
url = "http://blabla.com:8080/job/myproject/config.xml"
auth = ('user', 'pass')

# Read the XML file content
with open('new_config.xml', 'r') as file:
    payload = file.read()

# Set the headers
headers = {"Content-Type": "application/xml"}

# Make the POST request
response = requests.post(url, auth=auth, data=payload, headers=headers)

# Print the response status code and text for debugging
print(f'Status Code: {response.status_code}')
print(f'Response Text: {response.text}')
