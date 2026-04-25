
import requests

# Making a GET request
response = requests.get('https://api.github.com')

# Check the response status code
if response.status_code == 200:
    print("Success:", response.json())
else:
    print("Failed to retrieve data:", response.status_code)
