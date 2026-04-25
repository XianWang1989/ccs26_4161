
import requests

def send_post_request(url, data):
    # Force the connection to use IPv4
    proxies = {
        'http': 'http://127.0.0.1:80',
        'https': 'http://127.0.0.1:443',
    }

    try:
        response = requests.post(url, data=data, proxies=proxies)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        raise

# Example usage
url = "http://example.com/api"
data = {'key': 'value'}
send_post_request(url, data)
