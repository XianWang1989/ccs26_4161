
import requests

try:
    response = requests.get('https://api.github.com')
    print('Response code:', response.status_code)
except requests.exceptions.RequestException as e:
    print('Error:', e)
