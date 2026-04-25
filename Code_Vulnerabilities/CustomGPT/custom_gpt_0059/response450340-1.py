
import requests

# Define the URL and authentication
url = "http://user:pass@blabla.com:8080/job/myproject/config.xml"

# Read the new config file
with open("new_config.xml", "rb") as config_file:
    # Send the POST request to update config.xml
    response = requests.post(url, auth=('user', 'pass'), data=config_file, headers={"Content-Type": "application/xml"})

# Check the response
print(response.status_code)
print(response.text)
