
import requests

# Define the URL, authentication, and headers
url = "http://user:pass@blabla.com:8080/job/myproject/config.xml"
auth = ('user', 'pass')
headers = {"Content-Type": "application/xml"}

# Read the contents of new_config.xml
with open("new_config.xml", "rb") as file:
    # Send the POST request with the config's XML data
    response = requests.post(url, auth=auth, data=file, headers=headers)

# Check the response status
print(f"Response Code: {response.status_code}")
print(f"Response Text: {response.text}")
