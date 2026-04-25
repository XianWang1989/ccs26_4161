
import requests

url = 'https://httpbin.org/get'
response = requests.get(url)

if response.status_code == 200:
    print('Success:', response.json())
else:
    print('Failed:', response.status_code)
