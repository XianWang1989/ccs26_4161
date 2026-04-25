
import requests

# Example of using requests with SSL verification
try:
    response = requests.get('https://api.example.com/data', verify=True)
    print(response.json())
except requests.exceptions.SSLError as e:
    print("SSL error: ", e)
except Exception as e:
    print("An error occurred: ", e)
