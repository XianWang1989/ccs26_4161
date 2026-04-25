
import requests

# Define the URL and authentication
url = "http://blabla.com:8080/job/myproject/config.xml"
auth = ('user', 'pass')

# Open the new_config.xml file in binary read mode
with open("new_config.xml", "rb") as file:
    # Send the POST request
    response = requests.post(url, auth=auth, data=file, headers={"Content-Type": "application/xml"})

# Check the response
print(response.status_code)
print(response.text)  # Optional: Print the response text for more details
