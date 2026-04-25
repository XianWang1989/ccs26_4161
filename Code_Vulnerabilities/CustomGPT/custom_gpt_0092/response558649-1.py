
import requests

# Example GET request
response = requests.get('https://api.github.com')
print(response.status_code)
print(response.json())
