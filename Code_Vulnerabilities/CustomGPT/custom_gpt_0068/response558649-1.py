
import requests

# Example URL
url = 'https://api.github.com'

try:
    # Make a GET request
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        print('Request successful!')
        print('Response JSON:', response.json())
    else:
        print('Request failed with status code:', response.status_code)

except Exception as e:
    print('An error occurred:', str(e))
