
import requests

url = 'https://api.example.com/data'
response = requests.get(url)

if response.status_code == 200:
    print("Success:", response.json())
else:
    print("Failed to retrieve data:", response.status_code)
