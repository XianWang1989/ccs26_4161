
import requests

try:
    response = requests.get('https://api.github.com')
    print(response.json())
except requests.exceptions.SSLError as e:
    print("SSL Error:", e)
