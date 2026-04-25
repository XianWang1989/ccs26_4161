
import requests

url = "http://blabla.com:8080/job/myproject/config.xml"
auth = ('user', 'pass')

# Read the contents of the new_config.xml file
with open('new_config.xml', 'rb') as file:
    payload = file.read()  # Read the file as binary

headers = {
    "Content-Type": "application/xml"
}

# Perform the POST request
response = requests.post(url, auth=auth, data=payload, headers=headers)

# Check the response
print(f"Response Code: {response.status_code}")
if response.status_code == 200:
    print("Config updated successfully!")
else:
    print("Failed to update config:", response.text)
