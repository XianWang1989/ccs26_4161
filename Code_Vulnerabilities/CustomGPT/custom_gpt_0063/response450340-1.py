
import requests

# Specify the URL and authentication
url = "http://user:pass@blabla.com:8080/job/myproject/config.xml"

# Read the content of the new_config.xml file
with open("new_config.xml", "rb") as config_file:
    data = config_file.read()

# Set the headers
headers = {"Content-Type": "application/xml"}

# Make the POST request
response = requests.post(url, data=data, headers=headers)

# Print the response status code and any response text for debugging
print("Status Code:", response.status_code)
print("Response:", response.text)
