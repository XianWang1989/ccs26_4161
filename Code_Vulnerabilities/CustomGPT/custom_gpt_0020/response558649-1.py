
import requests

try:
    response = requests.get('https://api.github.com')
    response.raise_for_status()  # This raises an HTTPError if the response was not successful
    print(response.json())  # Print the JSON response
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
