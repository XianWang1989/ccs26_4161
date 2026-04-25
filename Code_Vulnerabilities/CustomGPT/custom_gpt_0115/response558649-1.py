
import requests

try:
    response = requests.get('https://api.github.com/events')
    print(response.status_code)
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
