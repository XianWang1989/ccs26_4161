
import requests

url = 'https://api.example.com/data'
try:
    response = requests.get(url)
    response.raise_for_status()  # Raises an error for 4xx/5xx responses
    print(response.json())  # Print the JSON response from the server
except requests.exceptions.RequestException as e:
    print(f'Error occurred: {e}')
