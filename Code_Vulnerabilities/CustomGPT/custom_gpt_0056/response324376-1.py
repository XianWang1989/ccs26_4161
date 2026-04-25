
import requests
from requests.exceptions import ConnectionError

url = 'http://example.com/api'  # Replace with your target URL
data = {'key': 'value'}  # Your payload

try:
    response = requests.post(url, json=data)
    response.raise_for_status()
    print('Success:', response.json())
except ConnectionError as e:
    print('ConnectionError:', e)
except Exception as e:
    print('An error occurred:', e)
