
import requests
try:
    response = requests.get('https://example.com')
    print('Status Code:', response.status_code)
    print('Response Body:', response.text)
except Exception as e:
    print('An error occurred:', str(e))
