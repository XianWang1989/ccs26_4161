
import requests

# Check the version of requests
print(requests.__version__)

# Try making a simple GET request
response = requests.get('https://api.github.com')
print(response.status_code)
