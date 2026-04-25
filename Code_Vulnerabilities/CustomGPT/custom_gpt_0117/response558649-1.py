
import requests

# Example of making a secure HTTPS request
url = 'https://api.github.com'
response = requests.get(url)

if response.status_code == 200:
    print('Success:', response.json())
else:
    print('Error:', response.status_code)
