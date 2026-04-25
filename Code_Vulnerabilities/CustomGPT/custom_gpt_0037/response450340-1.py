
import requests

url = "http://blabla.com:8080/job/myproject/config.xml"
auth = ('user', 'pass')

# Read the contents of the new_config.xml file
with open('new_config.xml', 'rb') as file:
    # Send the POST request with the file content as data
    r = requests.post(url, auth=auth, data=file, headers={"Content-Type": "application/xml"})

# Check the response
print(f"Response Code: {r.status_code}")
print(r.text)  # Print the response text for debugging
