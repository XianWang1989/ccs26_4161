
import requests

# This endpoint returns a JSON response
url = 'https://api.github.com'

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    data = response.json()  # Parse the JSON response
    print(data)  # Print the data
except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")
except Exception as e:
    print(f"An error occurred: {e}")
