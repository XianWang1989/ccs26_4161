
import requests

# Make a secure request to a website
response = requests.get('https://api.github.com')
print(response.json())
