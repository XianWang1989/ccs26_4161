
import requests

# Make a simple GET request
response = requests.get('https://api.github.com')

# Check the response
if response.status_code == 200:
    print('Success:', response.json())
else:
    print('Failed:', response.status_code)
