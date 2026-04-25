
import requests

url = "http://blabla.com:8080/job/myproject/config.xml"
auth = ('user', 'pass')

with open("new_config.xml", 'rb') as file:
    r = requests.post(url, auth=auth, data=file, headers={"Content-Type": "application/xml"})

print(f"Response code: {r.status_code}")
print(r.text)
