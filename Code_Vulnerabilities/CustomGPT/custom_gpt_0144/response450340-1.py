import requests

url = "http://blabla.com:8080/job/myproject/config.xml"
auth = ('user', 'pass')
headers = {"Content-Type": "application/xml"}

# Open the file in binary mode and send it as the request body
with open("new_config.xml", "rb") as file:
    response = requests.post(url, auth=auth, headers=headers, data=file)

print(response.status_code)
print(response.text)
