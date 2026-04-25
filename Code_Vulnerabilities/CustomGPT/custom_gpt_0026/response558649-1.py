
import requests

# Example of sending a GET request
response = requests.get('https://api.example.com/data')

if response.status_code == 200:
    print('Success:', response.json())
else:
    print('Failed to retrieve data:', response.status_code)
