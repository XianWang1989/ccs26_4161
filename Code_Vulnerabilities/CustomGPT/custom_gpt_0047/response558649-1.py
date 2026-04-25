
import requests

# Check requests version
print("Requests version:", requests.__version__)

# Example HTTPS request
try:
    response = requests.get('https://example.com')
    response.raise_for_status()  # Raises an error for bad responses
    print("Response content:", response.content)
except requests.exceptions.RequestException as e:
    print("An error occurred:", e)
