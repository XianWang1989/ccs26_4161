
import requests

url = "http://user:pass@blabla.com:8080/job/myproject/config.xml"
headers = {"Content-Type": "application/xml"}

with open("new_config.xml", "rb") as file:
    r = requests.post(url, headers=headers, data=file)

print(r.status_code)
print(r.text)
