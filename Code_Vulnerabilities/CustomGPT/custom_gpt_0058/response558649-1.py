
import requests

response = requests.get('https://api.github.com')
if response.status_code == 200:
    print("Successfully reached GitHub API")
    print(response.json())
else:
    print(f"Error: {response.status_code}")
