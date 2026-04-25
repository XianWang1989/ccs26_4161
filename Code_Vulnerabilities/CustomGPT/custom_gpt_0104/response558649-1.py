
import requests

try:
    response = requests.get('https://api.github.com')
    print(f"Status Code: {response.status_code}")
    print(f"Response Body: {response.json()}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
