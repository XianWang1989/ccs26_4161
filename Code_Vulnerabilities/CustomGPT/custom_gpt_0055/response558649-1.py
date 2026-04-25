
import requests

try:
    response = requests.get('https://api.example.com/data', verify=True)
    print(response.json())
except requests.exceptions.SSLError as e:
    print("SSL Error: ", e)
except requests.exceptions.RequestException as e:
    print("Request failed: ", e)
