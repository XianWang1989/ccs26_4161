
import requests

try:
    response = requests.get('https://api.github.com')
    print("Requests library is working! Status Code:", response.status_code)
except Exception as e:
    print("An error occurred:", e)
