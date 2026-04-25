
import requests

# Define the URL and authentication
url = "http://user:pass@blabla.com:8080/job/myproject/config.xml"

# Open the new configuration file in binary mode
with open("new_config.xml", 'rb') as file:
    # Send the POST request with binary data
    r = requests.post(url, auth=('user', 'pass'), data=file, headers={"Content-Type": "application/xml"})

# Check the response
print(f"Response Code: {r.status_code}")
print(f"Response Content: {r.content.decode()}")
