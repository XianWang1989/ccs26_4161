
import requests

try:
    response = requests.get('https://api.github.com')
    response.raise_for_status()  # Raise an error for bad responses
    print(response.json())  # Print the JSON response
except requests.exceptions.SSLError as ssl_error:
    print(f"SSL error occurred: {ssl_error}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
