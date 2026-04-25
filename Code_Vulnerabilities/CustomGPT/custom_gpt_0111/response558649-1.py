
import requests

# Make a GET request
response = requests.get('https://api.github.com')

# Check if the request was successful
if response.status_code == 200:
    print('Successful request!')
    print(response.json())
else:
    print('Request failed:', response.status_code)
