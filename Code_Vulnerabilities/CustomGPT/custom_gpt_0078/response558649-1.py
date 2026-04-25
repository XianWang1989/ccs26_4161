
import requests

# Example request to a secure URL
response = requests.get('https://api.example.com/data')

# Check if the request was successful
if response.status_code == 200:
    print('Data retrieved successfully:', response.json())
else:
    print('Failed to retrieve data:', response.status_code)
