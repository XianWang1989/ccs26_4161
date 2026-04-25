
import requests

# Set up a secure request
try:
    response = requests.get('https://example.com', verify=True)
    print(response.text)
except requests.exceptions.SSLError as e:
    print("SSL Error:", e)
