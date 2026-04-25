
import requests

# Define the URL, authentication, and the path to the new config file
url = "http://user:pass@blabla.com:8080/job/myproject/config.xml"

# Open the new_config.xml file and read its contents
with open("new_config.xml", "rb") as config_file:
    # Send the POST request with the file contents
    response = requests.post(url, auth=('user', 'pass'), data=config_file, headers={"Content-Type": "application/xml"})

# Print the response
print(f"Response Code: {response.status_code}")
print(f"Response Body: {response.text}")
