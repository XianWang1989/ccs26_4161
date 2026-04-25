
import requests

# Replace 'https://api.example.com' with the API endpoint you intend to call
url = 'https://api.example.com/data'

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses (e.g., 404, 500)
    data = response.json()  # Assuming the response is in JSON format
    print(data)
except requests.exceptions.RequestException as e:
    print(f'An error occurred: {e}')
