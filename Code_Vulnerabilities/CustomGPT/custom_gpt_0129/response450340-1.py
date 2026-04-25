
import requests

# Define the URL for the Jenkins job
url = "http://user:pass@blabla.com:8080/job/myproject/config.xml"

# Open the new_config.xml file and read its contents
with open("new_config.xml", "rb") as config_file:
    config_data = config_file.read()

# Set the headers
headers = {"Content-Type": "application/xml"}

# Make the POST request
r = requests.post(url, data=config_data, headers=headers)

# Print the response code and any response body
print(f"Response Code: {r.status_code}")
print("Response Body:", r.text)
