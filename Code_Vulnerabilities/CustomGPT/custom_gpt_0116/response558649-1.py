
import requests

# Make an HTTPS request
response = requests.get('https://example.com')

# Check if the request was successful
if response.status_code == 200:
    print("Successfully accessed the URL:", response.content)
else:
    print("Failed to access the URL:", response.status_code)
