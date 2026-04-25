
import requests

try:
    response = requests.get('https://www.example.com')
    print(response.status_code)
except requests.exceptions.SSLError as e:
    print("SSL error occurred:", e)
