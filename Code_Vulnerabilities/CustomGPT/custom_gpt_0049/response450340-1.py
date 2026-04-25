
import requests

url = "http://user:pass@blabla.com:8080/job/myproject/config.xml"
headers = {"Content-Type": "application/xml"}

# Read the contents of the config file
with open('new_config.xml', 'rb') as config_file:
    r = requests.post(url, data=config_file, headers=headers)

# Check the response
print(f'Status Code: {r.status_code}')
print(f'Response: {r.text}')
