
import requests

response = requests.get('https://api.github.com')
if response.status_code == 200:
    print('Success!', response.json())
else:
    print('Failed to retrieve data', response.status_code)
