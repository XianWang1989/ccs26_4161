
import requests

# Making a GET request
response = requests.get('https://api.example.com/data')

# Check if the request was successful
if response.status_code == 200:
    print("Data received:", response.json())
else:
    print("Error:", response.status_code)
