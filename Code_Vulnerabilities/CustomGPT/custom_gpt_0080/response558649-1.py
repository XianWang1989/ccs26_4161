
import requests

try:
    response = requests.get('https://httpbin.org/get')
    print('Response Status Code:', response.status_code)
    print('Response Body:', response.json())
except Exception as e:
    print('Error:', str(e))
