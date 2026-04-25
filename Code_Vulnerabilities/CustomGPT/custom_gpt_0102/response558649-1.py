
import requests

# Make a secure request
response = requests.get('https://api.github.com', verify=True)

print(response.status_code)
print(response.json())
