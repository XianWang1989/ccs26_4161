
import requests

# Example of making a GET request
response = requests.get('https://api.github.com')

# Print the status code
print(f'Status Code: {response.status_code}')

# Print the response JSON
print(response.json())
