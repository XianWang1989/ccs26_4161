
import requests

url = "http://blabla.com:8080/job/myproject/config.xml"
auth = ('user', 'pass')

# Open the XML file and read its contents
with open("new_config.xml", 'rb') as file:
    # 'data' should be the content of the file, not a dictionary
    r = requests.post(url, auth=auth, data=file, headers={"Content-Type": "application/xml"})

# Check the response
print(f"Response Code: {r.status_code}")
print(f"Response Body: {r.text}")
