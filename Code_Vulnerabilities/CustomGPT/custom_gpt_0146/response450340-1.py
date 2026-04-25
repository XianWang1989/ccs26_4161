
import requests

url = "http://user:pass@blabla.com:8080/job/myproject/config.xml"  # Auth can be included in the URL.
# Alternatively, you can keep the auth tuple if you don't want to include credentials in the URL
auth = ('user', 'pass')

# Read the content of the new_config.xml file
with open('new_config.xml', 'rb') as config_file:
    payload = config_file.read()  # Read file contents as binary

headers = {"Content-Type": "application/xml"}

# Make the POST request
r = requests.post(url, auth=auth, data=payload, headers=headers)

# Print the response status code and content for debugging
print("Status Code:", r.status_code)
print("Response:", r.text)
