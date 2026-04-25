
import requests

# Example request to fetch data from a URL
response = requests.get('https://api.example.com/data')

# Check if the request was successful
if response.status_code == 200:
    print("Data retrieved successfully!")
    print(response.json())  # Process the JSON data
else:
    print(f"Failed to retrieve data: {response.status_code}")
