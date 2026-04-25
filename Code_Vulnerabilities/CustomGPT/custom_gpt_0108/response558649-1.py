
import requests

# Make a secure request
response = requests.get('https://api.github.com', timeout=5)
print(response.status_code)
print(response.json())
