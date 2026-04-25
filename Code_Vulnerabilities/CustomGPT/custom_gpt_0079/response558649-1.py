
import requests

url = 'https://api.github.com/user'
response = requests.get(url)

if response.status_code == 200:
    print('Success:', response.json())
else:
    print('Error:', response.status_code)
