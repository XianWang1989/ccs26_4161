
import requests

# Basic GET request
response = requests.get('https://api.github.com')

# Check if the request was successful
if response.status_code == 200:
    print('Success:', response.json())
else:
    print('Failed to retrieve data:', response.status_code)
