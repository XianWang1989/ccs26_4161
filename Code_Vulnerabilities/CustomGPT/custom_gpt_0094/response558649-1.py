
import requests

# Make a GET request to a website
response = requests.get('https://api.github.com')

# Print the status code and response data
print(f"Status Code: {response.status_code}")
print(f"Response: {response.json()}")
