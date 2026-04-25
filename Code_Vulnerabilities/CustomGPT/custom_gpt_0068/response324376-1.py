
import requests

try:
    response = requests.post('http://example.com/api/endpoint', json={'key': 'value'})
    print(response.status_code)
    print(response.json())
except requests.exceptions.ConnectionError as e:
    print(f"Connection error occurred: {e}")
