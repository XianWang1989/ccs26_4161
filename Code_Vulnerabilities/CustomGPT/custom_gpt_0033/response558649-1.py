
import requests

try:
    response = requests.get('https://api.github.com')
    print('Status Code:', response.status_code)
    print('Response Body:', response.json())
except Exception as e:
    print('An error occurred:', e)
