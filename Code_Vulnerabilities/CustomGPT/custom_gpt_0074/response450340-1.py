
import requests

url = "http://blabla.com:8080/job/myproject/config.xml"
auth = ('user', 'pass')

# Read the contents of the new_config.xml file
with open('new_config.xml', 'rb') as config_file:
    # The data to send in the request
    data = config_file.read()

# Set the appropriate headers
headers = {"Content-Type": "application/xml"}

# Send the POST request
r = requests.post(url, auth=auth, data=data, headers=headers)

# Print the response status code and content for debugging
print(r.status_code)
print(r.text)
