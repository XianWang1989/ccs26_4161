
import requests

# Example GET request
response = requests.get('https://api.github.com')

# Print the response
if response.status_code == 200:
    print("Success:", response.json())
else:
    print("Failed to retrieve data:", response.status_code)
