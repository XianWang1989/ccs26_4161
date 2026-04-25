
import requests

url = "http://blabla.com:8080/job/myproject/config.xml"
auth = ('user', 'pass')

# Open the file in binary mode
with open('new_config.xml', 'rb') as file:
    headers = {"Content-Type": "application/xml"}
    r = requests.post(url, auth=auth, data=file, headers=headers)

# Check response
print(f"Response Code: {r.status_code}")
print(r.text)  # Optional: to see the response content
