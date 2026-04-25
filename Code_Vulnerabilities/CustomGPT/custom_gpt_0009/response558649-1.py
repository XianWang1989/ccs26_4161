
import requests

# Example of making a secure GET request
response = requests.get('https://api.example.com/data')
if response.status_code == 200:
    print(response.json())
else:
    print(f"Failed to retrieve data: {response.status_code}")
