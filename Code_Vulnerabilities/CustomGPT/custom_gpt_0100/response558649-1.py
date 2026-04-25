
import requests

url = 'https://api.example.com/data'
try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    print(response.json())  # Print the JSON response from the API
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
