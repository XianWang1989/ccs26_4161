
import requests

# Check if requests is installed and working
try:
    response = requests.get('https://api.github.com')
    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())
except Exception as e:
    print("An error occurred:", str(e))
