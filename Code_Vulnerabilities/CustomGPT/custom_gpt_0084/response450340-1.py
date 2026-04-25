
import requests

url = "http://blabla.com:8080/job/myproject/config.xml"
auth = ('user', 'pass')

# Read the contents of the new_config.xml file
with open('new_config.xml', 'rb') as file:
    payload = file.read()

headers = {
    "Content-Type": "application/xml"
}

# Make the POST request
response = requests.post(url, auth=auth, data=payload, headers=headers)

# Print the response status code
print(response.status_code)
print(response.text)  # Optional: to see the response body
