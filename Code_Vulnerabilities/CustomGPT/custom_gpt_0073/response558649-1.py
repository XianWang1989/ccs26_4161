
import requests

# Example of making a secure GET request
response = requests.get('https://api.example.com/data')
if response.status_code == 200:
    print('Data retrieved successfully:', response.json())
else:
    print(f'Error: {response.status_code}')
