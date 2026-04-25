
import requests

url = "http://user:pass@blabla.com:8080/job/myproject/config.xml"
headers = {"Content-Type": "application/xml"}

# Read the contents of the new_config.xml file
with open('new_config.xml', 'rb') as file:
    data = file.read()

# Make the POST request
response = requests.post(url, data=data, headers=headers)

# Print the response code to see if it was successful
print(response.status_code)
