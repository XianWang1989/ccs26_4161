
import requests

def send_post_request():
    url = 'http://example.com/api/endpoint/'
    data = {'key': 'value'}

    try:
        response = requests.post(url, json=data, timeout=5)
        response.raise_for_status()  # Raise an error for bad responses
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
