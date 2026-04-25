
import requests

# Example API call
response = requests.get('https://api.example.com/data', verify=True)
print(response.json())
