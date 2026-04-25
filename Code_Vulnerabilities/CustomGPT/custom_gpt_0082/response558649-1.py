
import requests

# Make a simple GET request
response = requests.get('https://api.github.com')
print(response.status_code)
print(response.json())
