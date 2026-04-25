
import requests

url = "http://user:pass@blabla.com:8080/job/myproject/config.xml"
headers = {"Content-Type": "application/xml"}

# Read the contents of the new_config.xml file
with open("new_config.xml", "rb") as config_file:
    r = requests.post(url, headers=headers, data=config_file)

# Check the response
print(f"Response Code: {r.status_code}")
print(f"Response Body: {r.text}")
