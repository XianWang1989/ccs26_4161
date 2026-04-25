
import requests

url = "http://user:pass@blabla.com:8080/job/myproject/config.xml"

# Read the XML file contents
with open('new_config.xml', 'rb') as file:
    # Send the HTTP POST request with the file content
    response = requests.post(url, auth=('user', 'pass'), data=file, headers={"Content-Type": "application/xml"})

# Output the response status code and any response text for debugging
print("Status Code:", response.status_code)
print("Response Body:", response.text)
