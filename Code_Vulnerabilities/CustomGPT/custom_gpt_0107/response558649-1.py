
import requests

# Example of making a secured request
try:
    response = requests.get('https://api.github.com')
    print('Response Status Code:', response.status_code)
except requests.exceptions.RequestException as e:
    print('Request failed:', e)
