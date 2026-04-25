
import requests

url = 'http://your.api.endpoint'
payload = {'key': 'value'}

response = requests.post(url, json=payload, headers={"Host": "your.api.endpoint"})
print(response.status_code)
