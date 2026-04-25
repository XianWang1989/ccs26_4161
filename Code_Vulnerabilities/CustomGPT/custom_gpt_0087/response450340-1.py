
import requests

url = "http://blabla.com:8080/job/myproject/config.xml"
auth = ('user', 'pass')

# Read the contents of new_config.xml to send as the payload
with open("new_config.xml", "rb") as config_file:
    # Send the file content in the data parameter
    r = requests.post(url, auth=auth, data=config_file, headers={"Content-Type": "application/xml"})

# Check the response status code
print(r.status_code)
print(r.text)
