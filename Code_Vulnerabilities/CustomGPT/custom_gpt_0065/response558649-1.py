
import requests

# Make a secure request to a website
url = 'https://api.github.com'
try:
    response = requests.get(url)
    response.raise_for_status()  # Check for HTTP errors
    print(response.json())  # Print the response JSON data
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
