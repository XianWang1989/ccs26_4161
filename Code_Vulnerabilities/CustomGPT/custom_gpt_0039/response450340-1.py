
import requests

# Define the URL, authentication, and headers
url = "http://user:pass@blabla.com:8080/job/myproject/config.xml"
headers = {"Content-Type": "application/xml"}

# Read the config file
with open("new_config.xml", "rb") as config_file:
    # Send the POST request
    r = requests.post(url, headers=headers, data=config_file)

# Check the response
print(r.status_code)
print(r.text)  # Optionally print the response text for more details
