
import requests

# Define the URL and authentication
url = "http://user:pass@blabla.com:8080/job/myproject/config.xml"

# Since the credentials are included in the URL above, you don't need to pass them separately.
# However, for better security, it's recommended to use auth parameter instead
auth = ('user', 'pass')

# Read the contents of the new_config.xml file
with open('new_config.xml', 'rb') as file:
    payload = file.read()  # Use 'rb' to read binary data

# Define content-type header for XML
headers = {"Content-Type": "application/xml"}

# Make the POST request
response = requests.post(url, auth=auth, data=payload, headers=headers)

# Check and print the response status code
print(f"Response Status Code: {response.status_code}")
print(response.text)  # Print the response content for debugging
