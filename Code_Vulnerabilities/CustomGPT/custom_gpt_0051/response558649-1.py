
import requests

# Example of a simple GET request
response = requests.get('https://api.github.com')

print("Status Code:", response.status_code)
print("Response Body:", response.json())
