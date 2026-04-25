
import requests

url = "http://user:pass@blabla.com:8080/job/myproject/config.xml"
headers = {"Content-Type": "application/xml"}

# Read the XML file contents
with open('new_config.xml', 'rb') as file:  # Open the file in binary read mode
    r = requests.post(url, headers=headers, data=file)

# Check the response
if r.status_code == 200:
    print("Configuration updated successfully.")
else:
    print(f"Failed to update configuration: {r.status_code}")
    print(r.text)  # Print the response text for debugging purposes
