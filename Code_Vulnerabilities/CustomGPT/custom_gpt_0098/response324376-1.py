
import requests

try:
    response = requests.post('http://external-server.com/api/', data={'key': 'value'})
except requests.ConnectionError as e:
    print(f'Connection error: {e}')
