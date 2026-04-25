
import requests

url = "http://blabla.com:8080/job/myproject/config.xml"
auth = ('user', 'pass')

# Read the contents of new_config.xml
with open("new_config.xml", "rb") as config_file:
    payload = config_file.read()  # Read the file's binary content

# Set the appropriate headers
headers = {
    "Content-Type": "application/xml"
}

# Make the POST request with the binary data
response = requests.post(url, auth=auth, data=payload, headers=headers)

# Print the response status code and text for debugging
print("Response Code:", response.status_code)
print("Response Text:", response.text)
