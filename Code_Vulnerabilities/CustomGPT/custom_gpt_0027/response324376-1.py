
import requests

def test_connection():
    try:
        response = requests.post('http://external-server-url/api/', data={'key': 'value'})
        print(response.status_code, response.content)
    except requests.ConnectionError as e:
        print(f'Connection Error: {e}')
