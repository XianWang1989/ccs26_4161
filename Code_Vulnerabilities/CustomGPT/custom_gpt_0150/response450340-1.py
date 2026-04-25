
import requests

url = "http://user:pass@blabla.com:8080/job/myproject/config.xml"
headers = {"Content-Type": "application/xml"}

# Read the contents of the new_config.xml file
with open('new_config.xml', 'rb') as config_file:
    response = requests.post(url, headers=headers, data=config_file)

# Check the response
if response.status_code == 200:
    print("Config updated successfully.")
else:
    print(f"Failed to update config. Status code: {response.status_code}, Response: {response.text}")
