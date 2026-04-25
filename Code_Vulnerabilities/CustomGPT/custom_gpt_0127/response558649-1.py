
import requests

# Test an HTTPS request to check for SSL configuration
response = requests.get('https://www.example.com')

print(response.status_code)
