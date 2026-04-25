
import requests

def send_post_request(url, data):
    try:
        # Specify the IP version to use (IPv4)
        response = requests.post(url, data=data, headers={'Host': 'example.com'}, allow_redirects=False)
        response.raise_for_status()  # Raise an error for HTTP errors
        return response.json()  # Assuming the response is JSON
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Example usage
url = 'http://external-server.com/api/endpoint'
data = {'key': 'value'}
send_post_request(url, data)
