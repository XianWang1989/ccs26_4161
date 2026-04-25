
import requests

def send_post_request(data):
    try:
        response = requests.post('http://<IPv4 Address>', json=data)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(e)

data = {'key': 'value'}
send_post_request(data)
