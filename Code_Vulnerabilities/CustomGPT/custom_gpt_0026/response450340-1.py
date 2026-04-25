
import requests

# Define the URL and authentication
url = "http://user:pass@blabla.com:8080/job/myproject/config.xml"

# Read the contents of the XML file
with open("new_config.xml", "rb") as file:
    xml_content = file.read()

# Define headers
headers = {"Content-Type": "application/xml"}

# Make the POST request
response = requests.post(url, data=xml_content, headers=headers)

# Print the response status code and text
print("Status Code:", response.status_code)
print("Response Text:", response.text)
