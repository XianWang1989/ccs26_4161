
import requests

# Check if the installation was successful
try:
    response = requests.get('https://api.github.com')
    print('Response status code:', response.status_code)
except Exception as e:
    print('An error occurred:', e)
