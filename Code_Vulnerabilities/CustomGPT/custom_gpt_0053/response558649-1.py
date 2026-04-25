
import requests

try:
    response = requests.get('https://www.example.com')
    print(f"Status Code: {response.status_code}")
    print("Content:", response.text[:100])  # Print the first 100 characters
except Exception as e:
    print("An error occurred:", e)
