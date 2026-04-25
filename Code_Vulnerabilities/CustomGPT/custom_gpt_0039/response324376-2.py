
import requests
import socket

# Function to send POST request
def send_post_request():
    url = 'http://example.com/api'
    data = {'key': 'value'}

    # Force using IPv4
    socket.setdefaultfamily(socket.AF_INET)

    try:
        response = requests.post(url, data=data)
        response.raise_for_status()  # Raises a HTTPError for bad responses
        print(response.text)
    except requests.exceptions.RequestException as e:
        print(f'An error occurred: {e}')

# Call the function
send_post_request()
